#!/usr/bin/env python3
"""
extract_refs.py - font-aware PDF -> Markdown extraction for the CSE110 reference books.

Why this exists
---------------
Plain `pdftotext` output loses everything an AI tutor needs: code indentation,
heading structure, tables, and it keeps running heads / hard line wraps.
Generic converters (MarkItDown, PyMuPDF4LLM) flatten code onto a single line.
These three books each use a distinct monospace font for code and distinct
fonts/sizes for headings, so we read the font information directly.

Usage
-----
    python extract_refs.py --cr CR.pdf --hf HF.pdf --li LIANG.pdf --out refs/md

Needs: pymupdf (pip install pymupdf).  Optional: english-words (hyphen joining).
"""
import argparse, collections, json, os, re, sys
import pymupdf

# --------------------------------------------------------------------------
# Book profiles
# --------------------------------------------------------------------------
MONO_RE = re.compile(r"Courier|Mono|Consolas|Typewriter", re.I)
BOLD_RE = re.compile(r"Bold|Black|Semibold|Heavy|Medium", re.I)
ITAL_RE = re.compile(r"Italic|Oblique|-It$|-It[A-Z]|Ital", re.I)

JAVA_TOKENS = set("""
abstract assert boolean break byte case catch char class const continue default do double else enum
extends final finally float for goto if implements import instanceof int interface long native new
package private protected public return short static strictfp super switch synchronized this throw
throws transient try void volatile while true false null var String System Math Scanner Object
Integer Double Boolean Character File PrintWriter main println print printf nextInt nextDouble next nextLine
length charAt equals compareTo substring indexOf toString valueOf args out in
""".split())

LIG = {"\ufb01": "fi", "\ufb02": "fl", "\ufb00": "ff", "\ufb03": "ffi", "\ufb04": "ffl",
       "\u2002": " ", "\u2003": " ", "\u2009": " ", "\u00a0": " ", "\u200b": ""}


def clean_text(s):
    for k, v in LIG.items():
        s = s.replace(k, v)
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", s)


class Profile:
    name = ""
    offset = 0          # pdf page number = printed page number + offset
    code_font = MONO_RE

    def is_mono(self, font):
        return bool(MONO_RE.search(font))

    # return True if the line is page furniture
    def drop(self, ln, H, W):
        return False

    # return heading level 1..4 or None
    def heading(self, ln):
        return None


class CR(Profile):
    name = "Complete Reference"
    offset = 35

    def drop(self, ln, H, W):
        f, y, t = ln["font"], ln["y0"], ln["text"].strip()
        if not t:
            return True
        if y < 46 and f.startswith("MyriadPro"):
            return True                      # running head
        if y > 600 and f.startswith("MyriadPro") and re.fullmatch(r"\d+", t):
            return True                      # folio on chapter-opening pages
        if ln["x0"] > 450 and re.fullmatch(r"(?i)part\s+[ivx]+", t):
            return True                      # margin thumb tab
        return False

    def heading(self, ln):
        f, sz = ln["font"], round(ln["size"])
        if f.startswith("MyriadPro-Semibold") and ln["y0"] > 46:
            return {17: 1, 16: 1, 15: 2, 14: 3, 13: 4}.get(sz)
        return None


class LI(Profile):
    name = "Liang"
    offset = 23

    def drop(self, ln, H, W):
        f, y, x, t = ln["font"], ln["y0"], ln["x0"], ln["text"].strip()
        if not t:
            return True
        if t == "\u25a0":
            return True                      # orphan bullet glyph
        if f.startswith("Helvetica") and ln["size"] <= 6.5:
            return True                      # indd file stamp
        if f.startswith("TimesTenLTStd"):
            return True                      # labels inside console screenshots
        if y < 75 and f.startswith("GoudySansPro") and ln["size"] >= 12.5 and \
                (re.match(r"^\d{1,4}\s", t) or re.search(r"\s\d{1,4}$", t)):
            return True                      # running head
        if f.startswith("TimesLTPro-Roman") and ln["size"] <= 8.8 and not ln["mono"]:
            return True                      # margin key-term glosses
        return False

    def heading(self, ln):
        f, sz, t = ln["font"], round(ln["size"]), ln["text"].strip()
        if f.startswith("GoudySansPro-Medium"):
            if sz >= 16:
                return 1
            if sz >= 13:
                return 2
            if sz >= 11:
                return 3
        if f.startswith("GoudySansPro-Bold") and sz >= 10 and re.match(r"^\d+\.\d+(\.\d+)?\s", t):
            return 3
        return None


class HF(Profile):
    name = "Head First Java"
    offset = 38

    def drop(self, ln, H, W):
        f, y, t = ln["font"], ln["y0"], ln["text"].strip()
        if not t:
            return True
        if f.startswith("ArialRoundedMTBold") and (y < 36 or y > H - 48):
            return True                      # running head / folio / "you are here"
        return False

    def heading(self, ln):
        f = ln["font"]
        if f.startswith("MarkerFelt") and round(ln["size"]) >= 16:
            return 2
        if f.startswith("Arial-Black") and round(ln["size"]) >= 13:
            return 3
        if f.startswith("EatwellTall") or f.startswith("ArialRoundedMTBold") and round(ln["size"]) >= 14:
            return 3
        return None


PROFILES = {"cr": CR(), "hf": HF(), "li": LI()}


# --------------------------------------------------------------------------
# Hyphen repair vocabulary
# --------------------------------------------------------------------------
class Vocab:
    def __init__(self):
        self.words, self.hyph = set(), set()
        try:
            from english_words import get_english_words_set
            self.words |= get_english_words_set(["web2"], lower=True)
        except Exception:
            pass

    def learn_page(self, page):
        for w in page.get_text("words"):
            t = clean_text(w[4]).replace("\u00ad", "")
            t = t.strip(".,;:!?()[]{}\"'\u201c\u201d\u2018\u2019").lower()
            if not t or t.endswith("-"):
                continue
            if "-" in t:
                self.hyph.add(t)
            elif t.isalpha():
                self.words.add(t)

    def join(self, left, right):
        """left ends with '-' (maybe followed by closing markup), right is the next line."""
        lm = re.search(r"-((?:\*+|`)?)\s*$", left)
        rm = re.match(r"^\s*((?:\*+|`)?)", right)
        lmark, rmark = lm.group(1), rm.group(1)
        if lmark and lmark == rmark:                 # emphasis spans the line break: drop both marks
            left, right = left[: lm.start() + 1] + "", right[rm.end():]
        elif lmark or rmark:
            return left.rstrip() + " " + right.lstrip()
        else:
            left, right = left.rstrip(), right.lstrip()
        m = re.search(r"([A-Za-z]+)-$", left)
        n = re.match(r"([A-Za-z]+)", right)
        if not (m and n):
            return left + " " + right
        a, b = m.group(1), n.group(1)
        joined, hyph = (a + b).lower(), (a + "-" + b).lower()
        if hyph in self.hyph:
            return left + right
        if joined in self.words:
            return left[:-1] + right
        if a.lower() in self.words and b.lower() in self.words:
            return left + right                      # genuine compound
        return left[:-1] + right


# --------------------------------------------------------------------------
# Page -> lines
# --------------------------------------------------------------------------
def fix_math(text, font):
    if "Dingbats" in font:
        return re.sub("[\ue000-\uf8ff]", "\u2022", text)
    if "PearsonMATH" in font:
        return text.replace("*", "\u00d7").replace("p", "\u03c0")
    return text


def get_lines(page, prof):
    d = page.get_text("dict", flags=pymupdf.TEXT_PRESERVE_WHITESPACE | pymupdf.TEXT_MEDIABOX_CLIP)
    lines = []
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            spans = [(fix_math(clean_text(s["text"]), s["font"]), s["font"], s["size"], s["flags"], s["bbox"])
                     for s in l["spans"] if s["text"]]
            if not spans:
                continue
            text = "".join(s[0] for s in spans)
            nonblank = [s for s in spans if s[0].strip()]
            prose = [s for s in nonblank if not prof.is_mono(s[1])]
            pool = prose or nonblank or spans
            dom = max(pool, key=lambda s: len(s[0].strip()))
            ln = dict(x0=l["bbox"][0], y0=l["bbox"][1], x1=l["bbox"][2], y1=l["bbox"][3],
                      spans=spans, text=text, font=dom[1], size=dom[2])
            ln["mono"] = bool(nonblank) and not prose
            lines.append(ln)
    return lines


def in_rect(ln, r, pad=2):
    cx, cy = (ln["x0"] + ln["x1"]) / 2, (ln["y0"] + ln["y1"]) / 2
    return r.x0 - pad <= cx <= r.x1 + pad and r.y0 - pad <= cy <= r.y1 + pad


def md_table(rows):
    rows = [[re.sub(r"\s+", " ", clean_text(c or "")).replace("|", "\\|").strip() for c in r] for r in rows]
    rows = [r for r in rows if any(r)]
    if len(rows) < 2:
        return None
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    # drop empty columns
    keep = [i for i in range(n) if any(r[i] for r in rows)]
    rows = [[r[i] for i in keep] for r in rows]
    if len(keep) < 2:
        return None
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * len(rows[0])]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def find_page_tables(page, lines):
    found = []
    try:
        tabs = page.find_tables().tables
    except Exception:
        return found
    for t in tabs:
        r = pymupdf.Rect(t.bbox)
        if r.width < 90 or r.height < 20 or t.row_count < 2 or t.col_count < 2:
            continue
        inside = [l for l in lines if in_rect(l, r)]
        if not inside:
            continue
        if sum(l["mono"] for l in inside) > 0.5 * len(inside):
            continue                                 # a code listing, not a table
        rows = t.extract()
        cells = [c for row in rows for c in row]
        if sum(1 for c in cells if c and c.strip()) < 0.5 * len(cells):
            continue
        md = md_table(rows)
        if md:
            found.append(dict(rect=r, md=md))
    return found


def find_figures(page, min_w=80, min_h=60, min_area=8000):
    figs = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"] == 1:
            r = pymupdf.Rect(b["bbox"])
            if r.width >= min_w and r.height >= min_h and r.width * r.height >= min_area and r.width * r.height < 0.85 * page.rect.width * page.rect.height:
                figs.append(r)
    return figs


# --------------------------------------------------------------------------
# Tab-stop tables (Head First lays tables out as loose text at shared y positions)
# --------------------------------------------------------------------------
def tab_table(lines):
    """Return (markdown, consumed_line_ids, y) or None."""
    ls = sorted(lines, key=lambda l: (l["y0"], l["x0"]))
    rows = []
    for l in ls:
        if rows and abs(l["y0"] - rows[-1][0]["y0"]) <= 3:
            rows[-1].append(l)
        else:
            rows.append([l])
    for r in rows:
        r.sort(key=lambda l: l["x0"])

    def tabular(r):
        return len(r) >= 3 and all(b["x0"] - a["x0"] >= 25 for a, b in zip(r, r[1:]))

    idx = [i for i, r in enumerate(rows) if tabular(r)]
    if len(idx) < 3:
        return None
    grid = []
    for x in sorted(round(l["x0"]) for i in idx for l in rows[i]):
        if not grid or x - grid[-1] > 6:
            grid.append(x)
    ncol = len(grid)
    if ncol < 3:
        return None

    def col_of(x):
        c = [k for k, g in enumerate(grid) if g <= x + 6]
        return max(c) if c else None

    first, last = idx[0], idx[-1]
    header, consumed, start = None, [], first
    for j in range(max(first - 4, 0), first):                   # header row sits a few rows above (take the topmost match)
        r = rows[j]
        if len(r) == 1 and abs(r[0]["x0"] - grid[0]) <= 6:
            parts = [p.strip() for p in re.split(r"\s{2,}|\t", r[0]["text"].replace("\t", "  ")) if p.strip()]
            if len(parts) == ncol:
                header, consumed, start = parts, list(r), j + 1
                break
    end = last
    while end + 1 < len(rows) and end + 1 - last <= 3 and all(abs(l["x0"] - grid[0]) <= 6 or col_of(l["x0"]) is not None for l in rows[end + 1]) \
            and not any(l["font"].startswith("Arial-Black") for l in rows[end + 1]):
        end += 1
    table = []
    for i in range(start, end + 1):
        r = rows[i]
        cells = [""] * ncol
        for l in r:
            for sp in l["spans"]:
                if not sp[0].strip():
                    continue
                ci = col_of(sp[4][0])
                ci = 0 if ci is None else ci
                ci = 0 if ci is None else ci
                cells[ci] = (cells[ci] + " " + sp[0].replace("\t", " ")).strip() if cells[ci] else sp[0].replace("\t", " ").strip()
        raw = [c for c in cells]
        for k in range(ncol):                                    # "64 bits     -huge to huge" in one cell
            pieces = [p.strip() for p in re.split(r"\s{3,}", raw[k]) if p.strip()]
            if len(pieces) > 1 and k + len(pieces) <= ncol and not any(raw[k + 1: k + len(pieces)]):
                for q, p in enumerate(pieces):
                    cells[k + q] = p
        cells = [re.sub(r"\s+", " ", c).strip() for c in cells]
        consumed.extend(r)
        if table and not cells[0] and any(cells):                # wrapped value continues the previous row
            tgt = max(k for k, c in enumerate(table[-1]) if c) if any(table[-1]) else ncol - 1
            table[-1][tgt] = (table[-1][tgt] + " " + " ".join(c for c in cells if c)).strip()
            continue
        if any(cells):
            table.append(cells)
    if len(table) < 3:
        return None
    rows_md = [header or [""] * ncol] + table
    md = ["| " + " | ".join(rows_md[0]) + " |", "|" + "---|" * ncol]
    md += ["| " + " | ".join(r) + " |" for r in rows_md[1:]]
    return "\n".join(md), {id(l) for l in consumed}, rows[start][0]["y0"]


# --------------------------------------------------------------------------
# Inline formatting
# --------------------------------------------------------------------------
def span_style(span, prof):
    text, font, size, flags, _ = span
    if "Dingbats" in font or "PearsonMATH" in font:
        return "plain"
    if prof.is_mono(font):
        return "code"
    bold = bool(BOLD_RE.search(font)) or bool(flags & 16)
    ital = bool(ITAL_RE.search(font)) or bool(flags & 2)
    if bold and ital:
        return "bi"
    return "b" if bold else ("i" if ital else "plain")


def render_inline(spans, prof, strip_fmt=False):
    groups = []
    for s in spans:
        st = "plain" if strip_fmt else span_style(s, prof)
        if st == "b" and isinstance(prof, CR) and s[2] <= 10.5:
            tok = s[0].strip()
            if tok and " " not in tok and (tok in JAVA_TOKENS or re.search(r"[(.=;\[\]_]", tok) or tok[0].islower()):
                st = "code"                          # Complete Reference sets inline code in bold
        if groups and groups[-1][0] == st:
            groups[-1][1] += s[0]
        else:
            groups.append([st, s[0]])
    out = []
    for st, txt in groups:
        core = txt.strip()
        if not core or st == "plain" or not re.search(r"\w", core):
            out.append(txt)
            continue
        lead, trail = txt[: len(txt) - len(txt.lstrip())], txt[len(txt.rstrip()):]
        mark = {"code": "`", "b": "**", "i": "*", "bi": "***"}[st]
        if st == "code":
            core = core.replace("`", "'")
        out.append(f"{lead}{mark}{core}{mark}{trail}")
    s = "".join(out)
    return re.sub(r"(\*\*|`|\*)\s*\1", "", s) if False else s


def collapse_marks(t):
    t = re.sub(r"`(\s*)`", r"\1", t)
    t = re.sub(r"\*\*(\s+)\*\*", r"\1", t)
    t = re.sub(r"(?<!\*)\*(\s+)\*(?!\*)", r"\1", t)
    return t


def plain(spans):
    return re.sub(r"\s+", " ", "".join(s[0] for s in spans)).strip()


# --------------------------------------------------------------------------
# Code blocks
# --------------------------------------------------------------------------
def code_text(lines):
    """Rebuild indentation from x positions and keep blank lines from y gaps."""
    cws = []
    for l in lines:
        for s in l["spans"]:
            n = len(s[0])
            if n >= 4:
                cws.append((s[4][2] - s[4][0]) / n)
    cw = sorted(cws)[len(cws) // 2] if cws else 5.1
    base = min(l["x0"] for l in lines)
    out, prev = [], None
    for l in lines:
        if prev is not None:
            pitch = l["y0"] - prev["y0"]
            nominal = max(prev["size"], 8) * 1.28
            blanks = int(round(pitch / nominal)) - 1
            out.extend([""] * max(0, min(blanks, 3)))
        txt = ""
        x_cursor = None
        for s in l["spans"]:
            t = s[0].replace("\t", "    ").replace("\u2018", "'").replace("\u2019", "'") \
                .replace("\u201c", '"').replace("\u201d", '"')
            if x_cursor is not None:
                gap = s[4][0] - x_cursor
                if gap > cw * 0.6 and not txt.endswith(" ") and not t.startswith(" "):
                    txt += " " * int(round(gap / cw))
            txt += t
            x_cursor = s[4][2]
        pad = int(round((l["x0"] - base) / cw))
        out.append((" " * pad + txt).rstrip())
        prev = l
    return out


def strip_gutter(code):
    """Liang prints line numbers in a gutter: ' 9      // Compute area'. Remove if sequential."""
    nums = []
    for c in code:
        m = re.match(r"^\s*(\d{1,3})(?:  |$)", c)
        nums.append(int(m.group(1)) if m else None)
    found = [n for n in nums if n is not None]
    if len(found) < 2 or len(found) < 0.6 * len([c for c in code if c.strip()]):
        return code, False
    ok = all(b - a in (1,) for a, b in zip(found, found[1:]))
    if not ok:
        return code, False
    out = []
    for c in code:
        m = re.match(r"^\s*\d{1,3}(?:  |$)", c)
        out.append(c[m.end():] if m else c)
    return out, True


def looks_java(code):
    t = "\n".join(code)
    return bool(re.search(r"[;{}]|\bclass\b|\bimport\b|\bpublic\b|\bint\b|\bvoid\b|System\.", t))


def fence(code):
    lang = "java" if looks_java(code) else "text"
    while code and not code[-1].strip():
        code = code[:-1]
    while code and not code[0].strip():
        code = code[1:]
    ind = min((len(c) - len(c.lstrip(" ")) for c in code if c.strip()), default=0)
    code = [c[ind:] for c in code]
    return "```" + lang + "\n" + "\n".join(code) + "\n```"


# --------------------------------------------------------------------------
# Page -> blocks
# --------------------------------------------------------------------------
CALLOUT_LABELS = {"Note", "Caution", "Tip", "Pedagogical Note", "Warning", "Key Point", "Programming Tip"}
BULLET_RE = re.compile(r"^\s*(?:([\u2022\u25aa\u25a0\u25cf\u25e6\u2023])\s*|([\u2013\u2014\-]|\d{1,2}[.)])\s+)(?=\S)")
HF_ASIDE_FONTS = ("ComicSans", "SkippySharp", "Futura", "UncleStinky", "ArialNarrow", "ArialMT", "Gilroy",
                  "Eatwell", "ArialRounded")


def hf_is_aside(ln):
    f = ln["font"]
    if f.startswith("MarkerFelt") and round(ln["size"]) >= 16:
        return False
    if f.startswith("Arial-Black") and round(ln["size"]) >= 13:
        return False
    if f.startswith("EatwellTall") and round(ln["size"]) >= 16:
        return False
    return f.startswith(HF_ASIDE_FONTS) or f.startswith(("MarkerFelt", "Arial-Black"))


def process_page(page, prof, vocab, figdir=None, figprefix="", save_figs=False):
    H, W = page.rect.height, page.rect.width
    raw = get_lines(page, prof)
    tables = find_page_tables(page, raw)
    figs = find_figures(page)
    is_hf = isinstance(prof, HF)

    kept, asides = [], []
    tabt = None
    if is_hf:
        cand = [l for l in raw if not prof.drop(l, H, W) and not any(in_rect(l, t["rect"]) for t in tables)
                and not l["font"].startswith(("Baskerville", "Courier", "MarkerFelt", "SkippySharp", "ComicSans"))
                and not l["mono"] and l["x1"] - l["x0"] < 140]
        tabt = tab_table(cand)
    for ln in raw:
        if prof.drop(ln, H, W):
            continue
        if tabt and id(ln) in tabt[1]:
            continue
        if any(in_rect(ln, t["rect"]) for t in tables):
            continue
        if any(in_rect(ln, f) for f in figs):
            if is_hf:
                asides.append(ln)
            continue
        if is_hf and hf_is_aside(ln) and prof.heading(ln) is None:
            asides.append(ln)
            continue
        kept.append(ln)

    # reading order
    if is_hf:
        kept.sort(key=lambda l: (0 if l["x0"] < W * 0.5 else 1, round(l["y0"] / 2), l["x0"]))
    else:
        kept.sort(key=lambda l: (round(l["y0"] / 2), l["x0"]))

    blocks = []
    cur = None          # current paragraph / list item
    code = None         # current code block lines
    pending_label = None
    xs = [round(l["x0"]) for l in kept if not l["mono"] and prof.heading(l) is None and l["size"] < 10.8]
    left_margin = collections.Counter(xs).most_common(1)[0][0] if xs else 0

    def flush():
        nonlocal cur, code
        if cur is not None:
            blocks.append(cur)
            cur = None
        if code is not None:
            blocks.append(dict(kind="code", text=code_text(code["lines"]), y=code["lines"][0]["y0"], col=code["col"]))
            code = None

    prev = None
    for ln in kept:
        col = (0 if ln["x0"] < W * 0.5 else 1) if is_hf else 0
        pitch = 1.22 * max(ln["size"], 8)
        hl = prof.heading(ln)
        t = plain(ln["spans"])

        # ---- headings
        if hl is not None:
            if cur is not None and cur["kind"] == "h" and cur["lvl"] == hl and abs(ln["y0"] - prev["y0"]) < 1.6 * pitch:
                cur["text"] += " " + t
            else:
                flush()
                cur = dict(kind="h", lvl=hl, text=t, y=ln["y0"], col=col)
            prev = ln
            continue

        # ---- code
        if ln["mono"]:
            if code is not None and (ln["y0"] - code["lines"][-1]["y0"]) <= 3.2 * pitch and code["col"] == col:
                code["lines"].append(ln)
            else:
                flush()
                code = dict(lines=[ln], col=col)
            prev = ln
            continue
        if code is not None:
            flush()

        # ---- callout label (Liang)
        if isinstance(prof, LI) and ln["font"].startswith("TimesLTPro-Bold") and round(ln["size"]) == 11 and t in CALLOUT_LABELS:
            flush()
            pending_label = t
            prev = ln
            continue
        quote = isinstance(prof, LI) and ln["font"].startswith("GoudySansPro-Book") and ln["size"] <= 9.6

        inline = render_inline(ln["spans"], prof)
        is_bullet = bool(BULLET_RE.match(t)) and not quote

        newp = True
        if cur is not None and cur["kind"] == "p" and prev is not None and not is_bullet:
            dy = ln["y0"] - prev["y0"]
            same_style = abs(prev["size"] - ln["size"]) < 0.6 and bool(cur.get("quote")) == quote
            indent_break = (not is_hf) and (ln["x0"] - left_margin > 8) and (prev["x0"] - left_margin <= 4 or prev["x0"] - left_margin > 8 and cur["x"] - left_margin > 8 and False) and not cur.get("bullet")
            if same_style and dy <= 1.32 * pitch and dy > -pitch and not indent_break and cur["col"] == col:
                newp = False
        if newp:
            flush()
            cur = dict(kind="p", text=inline, x=ln["x0"], y=ln["y0"], col=col, quote=quote, bullet=is_bullet,
                       size=ln["size"], label=pending_label if quote else None)
            if quote:
                pending_label = None
        else:
            cur["text"] = vocab.join(cur["text"].rstrip(), inline.lstrip()) if re.search(r"[A-Za-z]-(\*+|`)?\s*$", cur["text"]) \
                else (cur["text"].rstrip("\u00ad") + inline.lstrip() if cur["text"].endswith("\u00ad") else cur["text"].rstrip() + " " + inline.lstrip())
        prev = ln
    flush()

    # tables
    for t in tables:
        blocks.append(dict(kind="table", md=t["md"], y=t["rect"].y0, col=0))
    if tabt:
        blocks.append(dict(kind="table", md=tabt[0], y=tabt[2], col=1))
    # figures / asides (Head First)
    if is_hf:
        for k, r in enumerate(figs):
            if save_figs and figdir:
                os.makedirs(figdir, exist_ok=True)
                fn = f"{figprefix}_{k + 1}.png"
                page.get_pixmap(clip=r, dpi=120).save(os.path.join(figdir, fn))
                blocks.append(dict(kind="figure", path=f"figures/{fn}", y=r.y0 + 1e4, col=2))
        if asides:
            asides.sort(key=lambda l: (round(l["y0"] / 6), l["x0"]))
            txt = " / ".join(x for x in (plain(a["spans"]) for a in asides) if x)
            blocks.append(dict(kind="aside", text=txt, y=2e4, col=2))

    if not is_hf:
        blocks.sort(key=lambda b: b["y"])
    else:
        blocks.sort(key=lambda b: (b["col"], b["y"]))
    return blocks


# --------------------------------------------------------------------------
# Blocks -> markdown
# --------------------------------------------------------------------------
def block_to_md(b, prof):
    k = b["kind"]
    if k == "h":
        txt = re.sub(r"\s+", " ", b["text"]).strip()
        txt = txt.replace("**", "").replace("`", "")
        if is_checkpoint(b):
            m = re.match(r"^(\d+\.\d+\.\d+)\s+(.*)$", txt)
            return f"**Check Point {m.group(1)}** {m.group(2)}"
        return "#" * (b["lvl"] + 1) + " " + txt
    if k == "code":
        code, stripped = strip_gutter(list(b["text"]))
        b["gutter"] = stripped
        head = f"**{b['title']}**" + (" *(line N of the listing = Nth line of the block)*" if stripped else "") + "\n\n" if b.get("title") else ""
        return head + fence(code)
    if k == "table":
        return b["md"]
    if k == "figure":
        return f"![figure]({b['path']})"
    if k == "aside":
        return "> *Figure/sidebar text on this page:* " + b["text"]
    if k == "p":
        txt = collapse_marks(re.sub(r"[ \t]+", " ", b["text"]).strip().replace("\u00ad", ""))
        if b.get("bullet"):
            m = BULLET_RE.match(txt)
            if m:
                sym = m.group(1) or m.group(2)
                txt = ("- " if not sym[0].isdigit() else sym + " ") + txt[m.end():]
        if b.get("quote"):
            lab = f"**{b['label']}** " if b.get("label") else ""
            return "> " + lab + txt
        return txt
    return ""


def is_checkpoint(b):
    t = re.sub(r"\s+", " ", b.get("text", "")).strip()
    return b["kind"] == "h" and bool(re.match(r"^\d+\.\d+\.\d+\s", t)) and t.endswith((":", "?", "."))


def merge_pages(blocks_by_page, prof):
    """Flatten, merging code listings and paragraphs split across a page break."""
    flat = []
    for pno, blocks in blocks_by_page:
        for i, b in enumerate(blocks):
            b = dict(b, page=pno, first=(i == 0))
            if b["kind"] == "p":
                b["text"] = collapse_marks(b["text"])
            if flat and b["first"]:
                a = flat[-1]
                if a["kind"] == "code" and b["kind"] == "code" and a["col"] == b["col"]:
                    a["text"] = a["text"] + b["text"]
                    a.setdefault("pages", [a["page"]]).append(pno)
                    continue
                if a["kind"] == "p" and b["kind"] == "p" and not a.get("quote") and not b.get("quote") \
                        and not b.get("bullet") and not re.search(r"[.!?:;\)\u201d\"\u2019]\s*$", a["text"]) \
                        and re.match(r"^[a-z]", b["text"].lstrip("*` ")):
                    a["text"] = (a["text"].rstrip() + " " + b["text"].lstrip())
                    continue
            flat.append(b)
    # "Listing 2.1" caption (+ file name printed in the code font) -> title on the code block
    out, i = [], 0
    while i < len(flat):
        b = flat[i]
        if b["kind"] == "p" and i + 1 < len(flat) and flat[i + 1]["kind"] == "p" \
                and flat[i + 1]["text"].strip() == "**Key Point**" and b["text"].strip().startswith("*") \
                and b["text"].strip().endswith("*"):
            b = dict(b, quote=True, label="Key Point", text=b["text"].strip().strip("*"))
            out.append(b)
            i += 2
            continue
        if b["kind"] == "p" and re.fullmatch(r"\*\*Listing \d+\.\d+\*\*", b["text"].strip()) and i + 1 < len(flat) \
                and flat[i + 1]["kind"] == "code":
            nxt = flat[i + 1]
            title = b["text"].strip().strip("*")
            first = nxt["text"][0].strip() if nxt["text"] else ""
            if re.fullmatch(r"[\w$]+\.java", first):
                title += " " + first
                nxt["text"] = nxt["text"][1:]
            nxt["title"] = title
            out.append(nxt)
            i += 2
            continue
        out.append(b)
        i += 1
    return out


def join_blocks(parts):
    """Join markdown parts: list items and quote lines stay tight, everything else gets a blank line."""
    out = ""
    for i, p in enumerate(parts):
        if not p:
            continue
        if out:
            tight = (re.match(r"^(- |\d+\. )", p) and re.match(r"^(- |\d+\. )", out.rsplit("\n", 1)[-1]))
            out += "\n" + p if tight else "\n\n" + p
        else:
            out = p
    return out


# --------------------------------------------------------------------------
# Section filtering (Liang: the mapping is given by section number)
# --------------------------------------------------------------------------
def expand_sections(spec):
    """['2.4','2.9:intro','7.1-7.11'] -> (whole_ids, intro_ids)"""
    whole, intro = set(), set()
    for item in spec:
        if item.endswith(":intro"):
            intro.add(item[:-6])
        elif "-" in item:
            a, b = item.split("-")
            ch, x = a.rsplit(".", 1)
            for n in range(int(x), int(b.rsplit(".", 1)[1]) + 1):
                whole.add(f"{ch}.{n}")
        else:
            whole.add(item)
    return whole, intro


def filter_sections(flat, spec):
    whole, intro = expand_sections(spec)
    cur, out, seen = None, [], set()
    for b in flat:
        if b["kind"] == "h" and not is_checkpoint(b):
            m = re.match(r"^(\d+\.\d+(?:\.\d+)*)\s", re.sub(r"\s+", " ", b["text"]).strip())
            if m:
                cur = m.group(1)
            elif b["lvl"] == 1:
                cur = None
        ok = cur is not None and (cur in whole or cur in intro or any(cur.startswith(w + ".") for w in whole))
        if ok:
            seen.add(cur)
            out.append(b)
    return out, seen


# --------------------------------------------------------------------------
# Topic configuration  (printed page numbers; straight from "CSE110 Topic Wise Mapping.xlsx")
# --------------------------------------------------------------------------
TOPICS = [
    dict(id="intro_java", lessons="M1_L3", title="Introduction to Java",
         cr=[(10, 10), (27, 31), (34, 38)], hf=[(2, 2), (7, 9)],
         li=dict(pages=(11, 16), sections=["1.6", "1.7", "1.8"])),
    dict(id="variables", lessons="M2_L1, M2_L2, M2_L3", title="Variables & Data Types",
         cr=[(39, 45), (48, 55)], hf=[(49, 53)],
         li=dict(pages=(33, 70), sections=["2.4", "2.5", "2.6", "2.7", "2.8", "2.9:intro", "2.9.3", "2.10.1", "2.10.2", "2.16"],
                 note="2.9: Table 2.1 only. 2.9.3 and 2.10.1, 2.10.2 only (not all of 2.9 / 2.10).")),
    dict(id="references", lessons="(object references, pointers/values/addresses)", title="Object references (Head First only)",
         hf=[(54, 58)]),
    dict(id="operators", lessons="M3_L1, M3_L2", title="Operators",
         cr=[(67, 75), (80, 83), (85, 85)],
         li=dict(pages=(33, 110), sections=["2.9.2", "2.12", "2.14", "2.15", "3.2", "3.10", "3.14", "3.15"],
                 note="2.9.2: Table 2.3 only. 3.2: Table 3.1 only.")),
    dict(id="branching", lessons="M5_L1, M5_L2", title="Branching (if/else) and nested branching",
         cr=[(87, 90)], hf=[(15, 15)],
         li=dict(pages=(77, 90), sections=["3.3", "3.4", "3.5"])),
    dict(id="loops", lessons="M6_L1, M6_L2", title="Loops (while, for)",
         cr=[(95, 103)], hf=[(13, 14)],
         li=dict(pages=(155, 215), sections=["5.1", "5.2", "5.4", "5.6", "5.7"])),
    dict(id="nested_loops_break", lessons="M7", title="Nested loops, break, continue",
         cr=[(109, 111), (113, 114)],
         li=dict(pages=(155, 225), sections=["5.9", "5.12"])),
    dict(id="input_errors", lessons="M4_L1, M4_L2", title="User input (Scanner) and understanding errors",
         cr=[(13, 14), (691, 695)],
         li=dict(pages=(11, 30), sections=["1.10.1", "1.10.2", "1.10.3", "1.10.4", "1.10.5", "1.10.6"])),
    dict(id="string", lessons="M8", title="Strings",
         cr=[(47, 47), (65, 65), (160, 161), (483, 502)],
         li=dict(pages=(120, 150), sections=["4.3", "4.4", "4.5"], note="4.5 Case Studies is optional in the mapping.")),
    dict(id="array", lessons="M9", title="Arrays",
         cr=[(55, 57), (62, 62), (58, 61)], hf=[(59, 59)],
         li=dict(pages=(245, 280), sections=["7.1-7.11"]),
         note="CR pg 58-61 (multidimensional arrays) is OPTIONAL."),
    dict(id="sorting", lessons="M9", title="Sorting",
         li=dict(pages=(885, 895), sections=["23.1", "23.2", "23.3"])),
    dict(id="methods", lessons="M10", title="Methods",
         cr=[(123, 129)], hf=[(276, 278)],
         li=dict(pages=(200, 230), sections=["6.1-6.7", "6.9"])),
    dict(id="recursion", lessons="M11", title="Recursion",
         cr=[(147, 149)],
         li=dict(pages=(715, 745), sections=["18.1-18.9"])),
    dict(id="fileio", lessons="M12", title="File I/O",
         cr=[(315, 333)], hf=[(559, 569)],
         li=dict(pages=(445, 490), sections=["12.10", "12.11"]),
         note="CR pg 315-324 is OPTIONAL; the required part starts at 'Reading and Writing Files'."),
]
BOOKS = {"cr": "Java: The Complete Reference, 12th ed. (Schildt)",
         "hf": "Head First Java, 3rd ed. (Sierra, Bates, Gee)",
         "li": "Introduction to Java Programming and Data Structures, 12th ed. (Liang)"}


def pages_of(spec):
    out = []
    for a, b in spec:
        out.extend(range(a, b + 1))
    return out


def convert(doc, prof, book, printed_pages, vocab, outdir, topic_id, sections=None, save_figs=False):
    by_page = []
    for pn in printed_pages:
        pdfp = pn + prof.offset
        if not (1 <= pdfp <= len(doc)):
            continue
        blocks = process_page(doc[pdfp - 1], prof, vocab, figdir=os.path.join(outdir, "figures"),
                              figprefix=f"{book}_p{pn}", save_figs=save_figs)
        by_page.append((pn, blocks))
    flat = merge_pages(by_page, prof)
    seen = None
    if sections:
        flat, seen = filter_sections(flat, sections)
    parts, last = [], None
    for b in flat:
        if b["page"] != last:
            parts.append(f"<!-- {book.upper()} p.{b['page']} -->")
            last = b["page"]
        parts.append(block_to_md(b, prof))
    body = join_blocks(parts)
    return body, flat, seen



# --------------------------------------------------------------------------
# Full-book mode: one Markdown file per chapter (big chapters are chunked at section headings)
# --------------------------------------------------------------------------
def slug(t, n=48):
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower()
    return t[:n].strip("-")


def chapter_list(book, doc):
    toc = doc.get_toc()
    out = []
    if book == "cr":
        ents = [t for t in toc if t[0] <= 2]
        idx = [i for i, t in enumerate(ents) if t[0] == 2 and re.match(r"(Chapter|Appendix)\s", t[1])]
        for i in idx:
            end = ents[i + 1][2] - 1 if i + 1 < len(ents) else len(doc)
            m = re.match(r"(Chapter|Appendix)\s+(\w+)\s+(.*)", ents[i][1])
            out.append(dict(id=("ch%02d" % int(m.group(2))) if m.group(2).isdigit() else "app" + m.group(2).lower(),
                            title=m.group(3).strip(), start=ents[i][2], end=max(end, ents[i][2])))
    elif book == "hf":
        ents = [t for t in toc if t[0] == 1]
        for i, t in enumerate(ents):
            m = re.match(r"(Chapter|Appendix)\s+(\w+):\s*(.*)", t[1])
            if not (m or t[1] == "Intro"):
                continue
            end = ents[i + 1][2] - 1 if i + 1 < len(ents) else len(doc)
            if m:
                cid = ("ch%02d" % int(m.group(2))) if m.group(2).isdigit() else "app" + m.group(2).lower()
                title = m.group(3).strip()
            else:
                cid, title = "intro", "Intro"
            out.append(dict(id=cid, title=title, start=t[2], end=end))
    else:  # li: chapter number is printed in every page's file stamp (..._C05.indd)
        ch = collections.OrderedDict()
        for p in range(1, len(doc) + 1):
            m = re.search(r"_C(\d\d)\.indd", doc[p - 1].get_text())
            if m:
                ch.setdefault(m.group(1), [p, p])[1] = p
        for k, (a, b) in ch.items():
            title = ""
            for bl in process_page(doc[a - 1 + 1 if a + 1 <= b else a - 1], PROFILES["li"], Vocab()):
                if bl["kind"] == "h":
                    title = re.sub(r"\s+", " ", bl["text"]).strip()
                    break
            out.append(dict(id="ch" + k, title=title or "Chapter " + k, start=a, end=b))
    return out


def run_full(book, path, outdir, max_chars=90000, only=None):
    prof, doc = PROFILES[book], pymupdf.open(path)
    os.makedirs(os.path.join(outdir, book), exist_ok=True)
    chaps, toc = chapter_list(book, doc), []
    for c in chaps:
        if only and c["id"] not in only:
            continue
        pages = list(range(c["start"] - prof.offset, c["end"] - prof.offset + 1))
        vocab = Vocab()
        for pn in pages:
            vocab.learn_page(doc[pn + prof.offset - 1])
        body, flat, _ = convert(doc, prof, book, pages, vocab, os.path.join(outdir, book), c["id"], None,
                                save_figs=(book == "hf"))
        # chunk at h1/h2 boundaries
        chunks, cur, size = [], [], 0
        for b in flat:
            if b["kind"] == "h" and b["lvl"] <= 2 and size > max_chars:
                chunks.append(cur); cur, size = [], 0
            cur.append(b)
            size += len(b.get("text", "") if isinstance(b.get("text"), str) else "") + 80
        chunks.append(cur)
        files = []
        for n, ch in enumerate(chunks):
            parts, last = [], None
            for b in ch:
                if b["page"] != last:
                    parts.append(f"<!-- {book.upper()} p.{b['page']} -->")
                    last = b["page"]
                parts.append(block_to_md(b, prof))
            txt = join_blocks(parts)
            pgs = sorted({b["page"] for b in ch})
            if not pgs:
                continue
            name = f"{book}_{c['id']}_{slug(c['title'])}" + (f"_part{n + 1}" if len(chunks) > 1 else "") + ".md"
            hdr = ["---", f"book: \"{BOOKS[book]}\"", f"chapter: \"{c['id']} {c['title']}\"",
                   f"printed_pages: \"{pgs[0]}-{pgs[-1]}\"", f"pdf_offset: \"pdf page = printed page + {prof.offset}\"",
                   "generated_by: tools/extract_refs.py --full", "---\n"]
            with open(os.path.join(outdir, book, name), "w", encoding="utf-8") as f:
                f.write("\n".join(hdr) + f"# {c['id']} {c['title']}\n\n" + txt + "\n")
            heads = [(b["page"], b["lvl"], re.sub(r"\s+", " ", b["text"]).strip()) for b in ch
                     if b["kind"] == "h" and not is_checkpoint(b) and b["lvl"] <= 2]
            files.append(dict(file=f"{book}/{name}", pages=[pgs[0], pgs[-1]], chars=len(txt), headings=heads))
        toc.append(dict(id=c["id"], title=c["title"], pages=[pages[0], pages[-1]], files=files))
        print(book, c["id"], c["title"][:40], len(pages), "pages", flush=True)
    json.dump(toc, open(os.path.join(outdir, f"_toc_{book}.json"), "w"), indent=1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cr", required=True)
    ap.add_argument("--hf", required=True)
    ap.add_argument("--li", required=True)
    ap.add_argument("--out", default="refs/md")
    ap.add_argument("--only", help="comma separated topic ids")
    ap.add_argument("--chapters", help="comma separated chapter ids for --full, e.g. ch01,ch03")
    ap.add_argument("--full", choices=["cr", "hf", "li"], help="convert one whole book, chapter by chapter")
    a = ap.parse_args()
    if a.full:
        run_full(a.full, {"cr": a.cr, "hf": a.hf, "li": a.li}[a.full], a.out, only=set(a.chapters.split(",")) if a.chapters else None)
        return
    paths = {"cr": a.cr, "hf": a.hf, "li": a.li}
    docs = {k: pymupdf.open(v) for k, v in paths.items()}
    only = set(a.only.split(",")) if a.only else None
    os.makedirs(a.out, exist_ok=True)
    report = []
    for t in TOPICS:
        if only and t["id"] not in only:
            continue
        for book in ("cr", "hf", "li"):
            spec = t.get(book)
            if not spec:
                continue
            prof = PROFILES[book]
            sections = None
            if isinstance(spec, dict):
                pages = list(range(spec["pages"][0], spec["pages"][1] + 1))
                sections = spec["sections"]
                note = spec.get("note", "")
            else:
                pages = pages_of(spec)
                note = t.get("note", "") if book == "cr" and t["id"] == "array" else ""
            vocab = Vocab()
            for pn in pages:
                if 1 <= pn + prof.offset <= len(docs[book]):
                    vocab.learn_page(docs[book][pn + prof.offset - 1])
            body, flat, seen = convert(docs[book], prof, book, pages, vocab, a.out, t["id"], sections,
                                       save_figs=(book == "hf"))
            pgs = sorted({b["page"] for b in flat})
            hdr = ["---", f"topic: {t['id']}", f"lessons: \"{t['lessons']}\"", f"book: \"{BOOKS[book]}\"",
                   f"printed_pages: \"{pgs[0]}-{pgs[-1]}\"" if pgs else "printed_pages: none",
                   f"pdf_offset: \"pdf page = printed page + {prof.offset}\""]
            if sections:
                hdr.append("sections_in_scope: \"" + ", ".join(sections) + "\"")
            if note:
                hdr.append("note: \"" + note + "\"")
            hdr.append("generated_by: tools/extract_refs.py")
            hdr.append("---\n")
            fn = os.path.join(a.out, f"{t['id']}.{book}.md")
            with open(fn, "w", encoding="utf-8") as f:
                f.write("\n".join(hdr) + f"# {t['title']} - {BOOKS[book]}\n\n" + body + "\n")
            heads = [(b["page"], b["lvl"], re.sub(r"\s+", " ", b["text"]).strip()) for b in flat if b["kind"] == "h" and not is_checkpoint(b)]
            report.append(dict(topic=t["id"], book=book, file=os.path.basename(fn), chars=len(body), pages=pgs,
                               headings=heads, sections_found=sorted(seen) if seen is not None else None,
                               sections_wanted=sections))
            print(f"{os.path.basename(fn):32s} {len(body):7d} chars  pages {pgs[0] if pgs else '-'}-{pgs[-1] if pgs else '-'}")
    json.dump(report, open(os.path.join(a.out, "_report.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
