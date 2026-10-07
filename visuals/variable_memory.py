"""M2_L1 Variables - labeled jars in memory (Python diagram)."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, axes = plt.subplots(1, 3, figsize=(12, 4.2), facecolor='#fffbeb')
fig.suptitle("Variables = Labeled Jars on a Shelf (M2_L1)", fontsize=13, fontweight='bold', color='#713f12')

steps = [
    ("Step 1: Declare\nint age;", "?", "#fef3c7", "empty jar,\nlabel only"),
    ("Step 2: Initialize\nage = 17;", "17", "#bfdbfe", "jar now\nholds 17"),
    ("Step 3: Reassign\nage = 18;", "18", "#bbf7d0", "old value out,\n18 in!"),
]

for ax, (title, val, face, note) in zip(axes, steps):
    ax.set_facecolor('#fffbeb')
    # shelf
    ax.plot([0.1, 0.9], [0.18, 0.18], color='#92400e', lw=6, solid_capstyle='round')
    # jar body
    jar = patches.FancyBboxPatch((0.28, 0.2), 0.44, 0.5,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor=face, edgecolor='#713f12', linewidth=2.5)
    ax.add_patch(jar)
    # lid
    lid = patches.FancyBboxPatch((0.32, 0.7), 0.36, 0.08,
        boxstyle="round,pad=0.01,rounding_size=0.03",
        facecolor='#d6d3d1', edgecolor='#713f12', linewidth=2)
    ax.add_patch(lid)
    # label
    ax.text(0.5, 0.52, "age", ha='center', va='center', fontsize=13,
            fontweight='bold', color='#713f12',
            bbox=dict(facecolor='white', edgecolor='#713f12', boxstyle='round,pad=0.3'))
    # value
    ax.text(0.5, 0.33, val, ha='center', va='center', fontsize=22, fontweight='bold',
            color='#1e3a8a' if val != "?" else '#a8a29e')
    ax.text(0.5, 0.88, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#44403c')
    ax.text(0.5, 0.06, note, ha='center', va='center', fontsize=9, style='italic', color='#78716c')
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')

plt.tight_layout()
out = "visuals/variable_memory.png"
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Saved to {out}")
