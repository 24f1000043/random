import matplotlib.pyplot as plt
import seaborn as sns
# Removed: from PIL import Image # Not needed anymore
# Removed: import io # Not needed anymore

# 1. Determine the number of rows/columns in your correlation matrix
# Assuming 'N' is the size of your square matrix (e.g., 10x10)
# N = correlation_matrix.shape[0]

# 2. Calculate the required figure size for a 512x512 output
# We need to calculate the figure size (in inches) that, when multiplied
# by the DPI, results in a final image size of 512x512 pixels.
# Figure Size (in) = Target Pixels / DPI
# 512 / 100 = 5.12 inches.
# Using 5.12, 5.2, or even 5 inches is often a good starting point.
# Let's use 5.12 for maximum precision.

fig_size_inches = 512 / 100 # Results in 5.12
dpi_value = 100 # This is used as the resolution multiplier

# 3. Create the figure with the calculated dimensions
# Make sure the figure is a square (figsize=(X, X))
fig, ax = plt.subplots(figsize=(fig_size_inches, fig_size_inches), dpi=dpi_value)

# 4. Generate the heatmap
sns.heatmap(correlation_matrix, annot=True, fmt='.2f',
             cmap='coolwarm', center=0, ax=ax,
             # Optional: Add linewidths to ensure clear cell borders
             linewidths=0.5, linecolor='gray')

# 5. Save the figure directly as PNG, ensuring no cropping and high quality
# `bbox_inches='tight'` can sometimes be tricky for exact pixel sizes,
# so we rely on the figure size/DPI calculation for the resolution.
# `pad_inches=0` ensures no extra padding.

plt.savefig('heatmap.png', format='png', bbox_inches='tight', pad_inches=0, dpi=dpi_value)

plt.close()

# Removed all PIL Image code for resizing.
