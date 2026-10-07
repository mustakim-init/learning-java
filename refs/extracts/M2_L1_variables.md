# M2_L1 Variables — Distilled from Varsity Books (AI-cheap notes)

> Sources (mapped pages only — see `refs/` PDFs for full text, raw extracts in `refs/extracts_raw/`):
> - Complete Reference 12E, Ch3: book pg 39-45 + pg 48-55 (PDF p.74-80, 83-90)
> - Head First Java 3E, Ch3: book pg 49-53 (PDF p.87-91)
> - Liang 12E, Ch2: 2.4, 2.5, 2.6 (declaring, assignment, named constants)

## 1. Core message (all 3 books agree)
- **CR:** "Java is a strongly typed language. Every variable has a type... all assignments are checked for type compatibility. Any type mismatches are errors that must be corrected before the compiler will finish compiling."
- **HF:** "Java cares about type. It won't let you put a floating-point number into an integer variable. You must declare the type of your variable."
- Teaching line: the jar opening shape decides what fits (coin slot vs soup pot).

## 2. Declare + initialize (M2_L1 scope)
```java
int x;          // declaration only (empty jar with label)
x = 234;        // assignment
byte b = 89;   // declare + initialize in one line
boolean isFun = true;
double d = 3456.98;
char c = 'f';
int z = x;      // assign value of one variable to another
```
- Reassignment allowed: `y = y + 10;` (take out old value, put in new one).
- HF "spillage" rule: big cup -> small cup FAILS even if value fits: `int x = 24; byte b = x; // won't compile!` Compiler cares about cup SIZE, not current value. Small -> big always OK.

## 3. Naming rules (HF pg 53, safe subset)
1. Must start with letter, `_`, or `$` — NEVER a number.
2. After first char, numbers OK.
3. Must NOT be a Java keyword (`public, static, void, int, class...` — full list in HF pg 53 table).
- Convention (Liang 2.x): variables start lowercase, camelCase: `studentAge`, `radius`. Class names start uppercase.

## 4. The 8 primitives mnemonic (HF: "Be Careful! Bears Shouldn't Ingest Large Furry Dogs")
`boolean char byte short int long float double` — M2_L1 only needs: int, double, char, boolean, String (as preview). Full ranges table in CR pg 40 / HF pg 51 cups diagram.

## 5. `long`/`float` suffixes (HF note)
```java
long big = 3456789L;
float f = 32.5f;
```
Tell compiler explicitly with `L` / `f` (upper or lowercase).

## 6. What NOT to teach in M2_L1 (save for M2_L2)
- Type conversion/casting details, promotion rules, `final` constants depth, char arithmetic, full range tables memorization.
- References vs primitives depth (separate mini-lesson), arrays (M9).

## 7. Book exercise to reuse (HF pg 52 Sharpen Your Pencil)
Legal or not? (answers: 3,4,5,8,9,10 legal; 1,2,6-declared-no-value-use?,7,11,12 illegal)
```java
1. int x = 34.5;  2. boolean boo = x;  3. int g = 17;  4. int y = g;
5. y = y + 10;     6. short s;          7. s = y;        8. byte b = 3;
9. byte v = b;     10. short n = 12;    11. v = n;       12. byte k = 128;
```
