import matplotlib.pyplot as plt
import seaborn as sns

dpi = 100
fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=dpi)

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, ax=ax,
            square=True,
            cbar=False)  # Remove colorbar for perfect square

plt.tight_layout(pad=0.3)
plt.savefig('heatmap.png', dpi=dpi)
plt.close()
