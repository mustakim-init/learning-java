"""M1_L2 Loop Flowchart - Wash Dishes. Python diagram (Option B)."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(9, 8), facecolor='#f0fdfa')
ax.set_facecolor('#f0fdfa')

C_OVAL='#86efac'; C_RECT='#bfdbfe'; C_DIA='#fde68a'; C_ARROW='#0f766e'; C_LOOP='#dc2626'

def oval(x,y,t):
    b=patches.FancyBboxPatch((x-1.6,y-0.35),3.2,0.7,boxstyle="round,pad=0.1,rounding_size=0.35",
        facecolor=C_OVAL,edgecolor='#14532d',linewidth=2)
    ax.add_patch(b); ax.text(x,y,t,ha='center',va='center',fontsize=11,fontweight='bold',color='#14532d')
def rect(x,y,t):
    b=patches.FancyBboxPatch((x-1.8,y-0.4),3.6,0.8,boxstyle="square,pad=0.05",
        facecolor=C_RECT,edgecolor='#1e3a8a',linewidth=2)
    ax.add_patch(b); ax.text(x,y,t,ha='center',va='center',fontsize=10,fontweight='bold',color='#1e3a8a')
def diamond(x,y,t):
    d=patches.Polygon([[x,y+0.8],[x+2.2,y],[x,y-0.8],[x-2.2,y]],closed=True,
        facecolor=C_DIA,edgecolor='#78350f',linewidth=2)
    ax.add_patch(d); ax.text(x,y,t,ha='center',va='center',fontsize=10,fontweight='bold',color='#78350f')
def arrow(x1,y1,x2,y2,label=None,color=C_ARROW):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),
        arrowprops=dict(facecolor=color,edgecolor=color,width=2.5,headwidth=10,headlength=8))
    if label:
        mx,my=(x1+x2)/2,(y1+y2)/2
        ax.text(mx+0.4,my,label,fontsize=11,fontweight='bold',
            color='#15803d' if label=='YES' else '#6b7280',
            bbox=dict(facecolor='white',edgecolor='gray',boxstyle='round,pad=0.2'))

oval(5,9.5,"START")
arrow(5,9.1,5,8.5)
rect(5,8.0,"dishes = 3  (3 dirty dishes)")
arrow(5,7.55,5,7.0)
diamond(5,6.0,"dishes > 0 ?")
# YES branch down
arrow(5,5.1,5,4.4,label="YES")
rect(5,3.8,"Wash 1 dish\ndishes = dishes - 1")
# LOOP BACK arrow (red, on the right side)
ax.plot([6.8,7.5],[3.8,3.8],color=C_LOOP,lw=2.5)
ax.plot([7.5,7.5],[3.8,6.0],color=C_LOOP,lw=2.5)
ax.plot([7.5,7.2],[6.0,6.0],color=C_LOOP,lw=2.5)
ax.annotate('',xy=(7.0,6.0),xytext=(7.5,6.0),
    arrowprops=dict(facecolor=C_LOOP,edgecolor=C_LOOP,width=2.5,headwidth=10,headlength=8))
ax.text(7.5,5.0,"LOOP\nBACK ↩",color=C_LOOP,fontsize=10,fontweight='bold',ha='left',
    bbox=dict(facecolor='#fee2e2',edgecolor=C_LOOP,boxstyle='round,pad=0.3'))
# NO branch to END
ax.plot([2.8,1.5],[6.0,6.0],color=C_ARROW,lw=2.5)
arrow(1.5,6.0,1.5,2.4,label="NO")
oval(1.5,1.8,"END: clean!")

ax.text(5,2.2,"Trace: 3→2→1→0 then NO → END",ha='center',fontsize=10,
    style='italic',color='#0f766e',
    bbox=dict(facecolor='white',edgecolor='#0f766e',boxstyle='round,pad=0.4'))

ax.set_xlim(-1, 10.5); ax.set_ylim(0.8, 10.2); ax.axis('off')
plt.title("Loop Flowchart: While Dishes Remain, Keep Washing!\nBackward arrow = repeat (M1_L2)",
    fontsize=13,fontweight='bold',color='#134e4a',pad=15)
plt.tight_layout()
out="visuals/loop_flowchart.png"
plt.savefig(out,dpi=200,bbox_inches='tight',facecolor=fig.get_facecolor())
print(f"Saved to {out}")
