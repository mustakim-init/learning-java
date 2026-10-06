import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure
fig, ax = plt.subplots(figsize=(8, 10), facecolor='#0f172a')
ax.set_facecolor('#0f172a')

# Colors
COLOR_OVAL = '#38bdf8'       # Sky blue for Start/End
COLOR_RECT = '#a855f7'       # Purple for Process/Action
COLOR_DIAMOND = '#f59e0b'    # Amber for Decision
COLOR_PARALLEL = '#10b981'   # Emerald for Input/Output
COLOR_TEXT = '#ffffff'
COLOR_ARROW = '#94a3b8'

def draw_oval(ax, x, y, text):
    oval = patches.FancyBboxPatch((x - 1.8, y - 0.4), 3.6, 0.8,
                                  boxstyle="round,pad=0.2,rounding_size=0.4",
                                  facecolor=COLOR_OVAL, edgecolor='#7dd3fc', linewidth=2)
    ax.add_patch(oval)
    ax.text(x, y, text, ha='center', va='center', color='#0f172a', fontsize=12, fontweight='bold')

def draw_rect(ax, x, y, text):
    rect = patches.FancyBboxPatch((x - 2.2, y - 0.4), 4.4, 0.8,
                                  boxstyle="square,pad=0.1",
                                  facecolor=COLOR_RECT, edgecolor='#c084fc', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', color=COLOR_TEXT, fontsize=11, fontweight='bold')

def draw_diamond(ax, x, y, text):
    diamond = patches.Polygon([[x, y + 0.6], [x + 2.2, y], [x, y - 0.6], [x - 2.2, y]],
                              facecolor=COLOR_DIAMOND, edgecolor='#fde68a', linewidth=2)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', color='#0f172a', fontsize=11, fontweight='bold')

def draw_arrow(ax, x1, y1, x2, y2, label=None):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(facecolor=COLOR_ARROW, edgecolor=COLOR_ARROW, width=2, headwidth=8))
    if label:
        mid_x = (x1 + x2) / 2 + 0.3
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y, label, color='#38bdf8', fontsize=11, fontweight='bold')

# Draw Flowchart: Making a Cup of Tea
# 1. Start
draw_oval(ax, 5, 9.2, "START: Make Tea")

draw_arrow(ax, 5, 8.6, 5, 7.8)

# 2. Boil Water
draw_rect(ax, 5, 7.4, "Boil water in kettle")

draw_arrow(ax, 5, 6.9, 5, 6.1)

# 3. Add tea bag to cup
draw_rect(ax, 5, 5.7, "Put tea bag in cup")

draw_arrow(ax, 5, 5.2, 5, 4.4)

# 4. Pour hot water
draw_rect(ax, 5, 4.0, "Pour boiling water into cup")

draw_arrow(ax, 5, 3.5, 5, 2.7)

# 5. Decision: Want Sugar?
draw_diamond(ax, 5, 2.1, "Want Sugar?")

# Decision branches
# YES -> Add Sugar
draw_arrow(ax, 7.2, 2.1, 8.2, 2.1, label="YES")
draw_rect(ax, 8.5, 0.9, "Add sugar")
# Arrow down from sugar
ax.plot([7.2, 8.5], [2.1, 2.1], color=COLOR_ARROW, lw=2)
ax.plot([8.5, 8.5], [2.1, 1.4], color=COLOR_ARROW, lw=2)
draw_arrow(ax, 8.5, 1.4, 8.5, 1.3)

# NO branch continues down
draw_arrow(ax, 5, 1.5, 5, 0.7, label="NO")

# 6. Stir and Enjoy
draw_rect(ax, 5, 0.3, "Stir and Enjoy your tea!")

# Connect YES branch into Stir
ax.plot([8.5, 8.5], [0.4, -0.3], color=COLOR_ARROW, lw=2)
ax.plot([8.5, 5.0], [-0.3, -0.3], color=COLOR_ARROW, lw=2)
draw_arrow(ax, 5.0, -0.3, 5.0, -0.7)

# 7. End
draw_oval(ax, 5, -1.2, "END")

# Plot configuration
ax.set_xlim(0, 11)
ax.set_ylim(-2.2, 10.5)
ax.axis('off')

# Title & Subtitle
plt.title("Real-World Flowchart: How to Make Tea\nCSE110 Module 1 — Problem Solving Step-by-Step",
          color='#38bdf8', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
output_path = "visuals/tea_flowchart.png"
plt.savefig(output_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Diagram successfully saved to {output_path}!")
