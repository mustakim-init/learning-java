"""M1_L2 Decision Flowchart - Even or Odd? Python diagram (Option B)."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(9, 7), facecolor='#fefce8')
ax.set_facecolor('#fefce8')

C_OVAL = '#86efac'
C_RECT = '#bfdbfe'
C_DIA = '#fde68a'
C_PARA = '#c7d2fe'
C_ARROW = '#713f12'

def oval(x, y, text):
    b = patches.FancyBboxPatch((x-1.5, y-0.35), 3.0, 0.7,
        boxstyle="round,pad=0.1,rounding_size=0.35",
        facecolor=C_OVAL, edgecolor='#14532d', linewidth=2)
    ax.add_patch(b)
    ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color='#14532d')

def para(x, y, text):
    poly = patches.Polygon([[x-1.7, y+0.35],[x+1.3, y+0.35],[x+1.7, y-0.35],[x-1.3, y-0.35]],
        closed=True, facecolor=C_PARA, edgecolor='#1e1b4b', linewidth=2)
    ax.add_patch(poly)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#1e1b4b')

def rect(x, y, text):
    b = patches.FancyBboxPatch((x-1.5, y-0.35), 3.0, 0.7,
        boxstyle="square,pad=0.05", facecolor=C_RECT, edgecolor='#1e3a8a', linewidth=2)
    ax.add_patch(b)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#1e3a8a')

def diamond(x, y, text):
    d = patches.Polygon([[x, y+0.7],[x+2.0, y],[x, y-0.7],[x-2.0, y]],
        closed=True, facecolor=C_DIA, edgecolor='#78350f', linewidth=2)
    ax.add_patch(d)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='#78350f')

def arrow(x1, y1, x2, y2, label=None, color=C_ARROW):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(facecolor=color, edgecolor=color, width=2.5, headwidth=10, headlength=8))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx+0.35, my, label, fontsize=11, fontweight='bold',
                color='#15803d' if label=='YES' else '#dc2626',
                bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round,pad=0.2'))

# Layout (top to bottom)
oval(5, 9, "START")
arrow(5, 8.6, 5, 8.0)
para(5, 7.5, "Input a number")
arrow(5, 7.1, 5, 6.5)
diamond(5, 5.6, "number % 2 == 0 ?")
# YES left branch
ax.plot([3.2, 2.0], [5.6, 5.6], color=C_ARROW, lw=2.5)
arrow(2.0, 5.6, 2.0, 4.4, label="YES")
rect(2.0, 3.9, 'Print "Even"')
arrow(2.0, 3.5, 2.0, 2.6)
ax.plot([2.0, 5.0], [2.6, 2.6], color=C_ARROW, lw=2.5)
# NO right branch
ax.plot([6.8, 8.0], [5.6, 5.6], color=C_ARROW, lw=2.5)
arrow(8.0, 5.6, 8.0, 4.4, label="NO")
rect(8.0, 3.9, 'Print "Odd"')
arrow(8.0, 3.5, 8.0, 2.6)
ax.plot([8.0, 5.0], [2.6, 2.6], color=C_ARROW, lw=2.5)
arrow(5.0, 2.6, 5.0, 2.0)
oval(5, 1.5, "END")

ax.set_xlim(0, 10)
ax.set_ylim(0.5, 10)
ax.axis('off')
plt.title("Decision Flowchart: Even or Odd?\nDiamond = YES / NO fork in the road (M1_L2)",
          fontsize=13, fontweight='bold', color='#713f12', pad=15)
plt.tight_layout()
out = "visuals/decision_flowchart.png"
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Saved to {out}")
