import matplotlib.pyplot as plt
import seaborn as sns

# Set exact dimensions for square output
dpi = 100
fig_size = 5.12  # 512 pixels / 100 dpi = 5.12 inches

fig, ax = plt.subplots(figsize=(fig_size, fig_size), dpi=dpi)

# Create heatmap with square cells
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, ax=ax,
            square=True,  # This ensures square cells
            cbar_kws={'shrink': 0.8})

# Remove extra whitespace
plt.tight_layout(pad=0.5)

# Save WITHOUT bbox_inches='tight' to preserve dimensions
plt.savefig('heatmap.png', dpi=dpi, pad_inches=0.1)
plt.close()
