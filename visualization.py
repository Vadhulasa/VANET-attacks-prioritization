import matplotlib.pyplot as plt
import seaborn as sns

from prioritization import attack_prioritization

# Sort the data based on priority score (same as in line graph)
attack_prioritization = attack_prioritization.sort_values(by="Priority Score", ascending=False)

# Adjust figure size dynamically based on the number of classes
plt.figure(figsize=(12, max(5, 0.4 * len(attack_prioritization))))

# Create a bar plot (same order as line graph)
sns.barplot(
    data=attack_prioritization,
    x="Specific Class",
    y="Priority Score",
    color="red"
)

# Add proper headings and labels
plt.xlabel("Specific Class")
plt.ylabel("Priority Score")
plt.title("Attack Prioritization Based on Specific Class", fontsize=14, fontweight='bold')

plt.xticks(rotation=30)
plt.tight_layout()

#Save the figure
plt.savefig("bar_plot.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Line graph visualization
plt.figure(figsize=(12, 6))

# Create a line plot with markers
sns.lineplot(
    data=attack_prioritization,
    x="Specific Class",
    y="Priority Score",
    marker="o",
    linewidth=2,
    markersize=8,
    color="red"
)

# Labeling the graph
plt.xticks(rotation=45, ha='right')  # Rotate labels for readability
plt.xlabel("Specific Class")
plt.ylabel("Priority Score")
plt.title("Attack Prioritization Based on Specific Class")
plt.grid(True, linestyle="--", alpha=0.6)

#Save the figure
plt.savefig("line_plot.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()