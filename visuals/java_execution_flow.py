"""M1_L3 Java execution flow - Python diagram (clear arrows)."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 4.8), facecolor='#0f172a')
ax.set_facecolor('#0f172a')

def box(x, y, title, sub, face, edge, tcolor='#0f172a'):
    b = patches.FancyBboxPatch((x-1.25, y-0.6), 2.5, 1.2,
        boxstyle="round,pad=0.05,rounding_size=0.2",
        facecolor=face, edgecolor=edge, linewidth=2)
    ax.add_patch(b)
    ax.text(x, y+0.22, title, ha='center', va='center', fontsize=11, fontweight='bold', color=tcolor)
    ax.text(x, y-0.28, sub, ha='center', va='center', fontsize=8, color=tcolor)

def arrow(x1, x2, y, label):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
        arrowprops=dict(facecolor='white', edgecolor='white', width=2.5, headwidth=10, headlength=8))
    ax.text((x1+x2)/2, y+0.32, label, ha='center', fontsize=8, fontweight='bold', color='#fde68a',
        bbox=dict(facecolor='#1e293b', edgecolor='#fde68a', boxstyle='round,pad=0.25'))

# 4 boxes left to right
box(1.5, 2.0, "You write", "HelloWorld.java", '#fde68a', '#f59e0b')
box(4.5, 2.0, "javac", "proofreader", '#fca5a5', '#dc2626')
box(7.5, 2.0, "HelloWorld.class", "robot language", '#c4b5fd', '#7c3aed')
box(10.5, 2.0, "java", "robot runs", '#86efac', '#16a34a')

arrow(2.75, 3.25, 2.0, "write")
arrow(5.75, 6.25, 2.0, "javac HelloWorld.java")
arrow(8.75, 9.25, 2.0, "java HelloWorld")

ax.text(5.6, 0.55, 'OK? YES -> make .class   |   NO (missing ; typo) -> RED error, stop and fix!',
    ha='center', fontsize=9, color='#fca5a5',
    bbox=dict(facecolor='#1e293b', edgecolor='#dc2626', boxstyle='round,pad=0.4'))
ax.text(9.7, 0.55, 'Output: Hello, I am learning Java!',
    ha='center', fontsize=9, color='#86efac',
    bbox=dict(facecolor='#1e293b', edgecolor='#16a34a', boxstyle='round,pad=0.4'))

ax.set_xlim(0, 12); ax.set_ylim(0, 3.4); ax.axis('off')
plt.title("How Java Runs: write -> javac (check) -> java (run)  (M1_L3)",
    color='white', fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
out = "visuals/java_execution_flow.png"
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Saved to {out}")
