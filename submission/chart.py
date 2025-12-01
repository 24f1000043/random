import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Calculate dimensions based on your correlation matrix
n_vars = len(correlation_matrix)
cell_size = 60  # pixels per cell
total_size = n_vars * cell_size + 100  # add margin for labels

# Ensure it's within 400-512 range
total_size = min(512, max(400, total_size))

dpi = 100
fig_size = total_size / dpi

fig, ax = plt.subplots(figsize=(fig_size, fig_size), dpi=dpi)

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, ax=ax,
            square=True,
            linewidths=0.5,
            cbar_kws={'shrink': 0.85})

plt.tight_layout(pad=0.4)
plt.savefig('heatmap.png', dpi=dpi, format='png')
plt.close()

print(f"Saved heatmap as {total_size}x{total_size} pixels")
