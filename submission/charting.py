import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Create a mapping to simplify labels
# This changes "Visits" -> "A", "Avg_Spend" -> "B", etc.
label_mapping = {col: chr(65 + i) for i, col in enumerate(correlation_matrix.columns)}
simplified_matrix = correlation_matrix.rename(index=label_mapping, columns=label_mapping)

# Print the mapping so you can include it in your README if needed
print("Label Mapping:", label_mapping)

# 2. Setup the figure for exact 512x512 pixels
# 5.12 inches * 100 dpi = 512 pixels
fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)

# 3. Create the heatmap
# square=True ensures cells are perfect squares
# annot_kws={"size": 10} ensures the numbers inside don't touch borders
sns.heatmap(simplified_matrix, 
            annot=True, 
            fmt='.2f', 
            cmap='coolwarm', 
            center=0, 
            ax=ax,
            square=True,
            cbar=True,
            annot_kws={"size": 10}) # Adjust font size to prevent overlap

# 4. Clean up axes
plt.xticks(rotation=0) # Keep x-axis labels straight (A, B, C...)
plt.yticks(rotation=0) # Keep y-axis labels straight

# 5. Save directly without resizing
# bbox_inches='tight' clips whitespace, so we use pad_inches=0.1 to stay safe
plt.savefig('heatmap.png', dpi=100, bbox_inches='tight', pad_inches=0.1)
plt.close()
