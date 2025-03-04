import matplotlib.pyplot as plt

# Data for products
product_names = [
    "Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat white", 
    "Affogato", "Caramel macchiato", "Misto", "Cortado", "Black tea", "Green tea", 
    "Sour tea", "Mint tea", "Earl grey tea", "Ginger tea", "Chocolate cake", 
    "Lemon cake", "Carrot cake", "Strawberry cake", "Red velvet cake", "Cheesecake", 
    "Chocolate milkshake", "Vanilla milkshake", "Coffee milkshake", "Strawberry milkshake", 
    "Banana milkshake", "Strawberry banana smoothie", "Chocolate banana smoothie", 
    "Mango smoothie", "Peanut butter banana smoothie", "Ice tea", "Ice coffee", 
    "Lemonade", "Mojito", "Frappuccino", "Honey & milk", "Hot chocolate", "Chocolate milk"
]

product_values = [
    120, 48, 84, 72, 36, 30, 12, 15, 48, 9, 6, 96, 51, 12, 12, 15, 3, 33, 27, 
    15, 18, 24, 27, 42, 21, 12, 21, 27, 33, 21, 24, 3, 9, 21, 36, 30, 12, 21, 27, 24
]

# Data for ingredients
ingredient_names = [
    "Espresso Beans", "Milk", "Water", "Dried hibiscus flowers", "Cream", 
    "Chocolate Syrup", "Baking soda", "Black tea loose leaf", "Green tea loose leaf", 
    "Dried mint leaf", "Dried ginger root", "Honey", "Ground cinnamon", 
    "Graham cracker crumbs", "All-purpose flour", "Sugar", "Salt", "Cocoa powder", 
    "Baking powder", "Eggs", "Unsalted butter", "Vanilla Extract", "Ground ginger", 
    "Lemon juice", "Vegetable oil", "Grated carrots", "Cream cheese", "Ice-cream", 
    "Strawberries", "Yogurt", "Caramel sauce", "Peanut butter", "Mango", "Banana"
]

ingredient_values = [
    12, 129, 133, 1, 19, 5, 1, 2, 1, 1, 1, 16, 1, 9, 27, 32, 5, 5, 8, 33, 41, 17, 
    1, 30, 17, 9, 9, 21, 27, 9, 2, 1, 14, 17
]

# Common styling
common_style = {
    "font.size": 2,
    "axes.titlesize": 12,
    "axes.labelsize": 20,
    "legend.fontsize": 9,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
}

plt.rcParams.update(common_style)

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1, 1]})

# Plot for products
bars1 = axes[0].barh(product_names, product_values, color='lightblue', edgecolor='black', linewidth=0.5)
axes[0].grid(axis='x', linestyle='--', alpha=0.6)
axes[0].invert_yaxis()

axes[0].tick_params(axis='x', bottom=True, top=True, labelbottom=True, labeltop=True)
axes[1].tick_params(axis='x', bottom=True, top=True, labelbottom=True, labeltop=True)

# Extend x-axis limits to make room for text
axes[0].set_xlim(0, max(product_values) + 10)
# Add values on top of bars for products
for bar in bars1:
    width = bar.get_width()
    axes[0].text(width + 2, bar.get_y() + bar.get_height() / 2, str(width), va='center', fontsize=9)

# Plot for ingredients
bars2 = axes[1].barh(ingredient_names, ingredient_values, color='lightgreen', edgecolor='black', linewidth=0.5)
axes[1].grid(axis='x', linestyle='--', alpha=0.6)
axes[1].invert_yaxis()

axes[1].set_xlim(0, max(ingredient_values) + 6)
# Add values on top of bars for ingredients
for bar in bars2:
    width = bar.get_width()
    axes[1].text(width + 2, bar.get_y() + bar.get_height() / 2, str(width), va='center', fontsize=9)

# Adjust layout and spacing
plt.tight_layout(w_pad=3)  # Add spacing between the subplots

# Save the combined plot in high resolution for publication
#plt.savefig("Combined_OptimalSolutions_Final2200.svg", format='svg',dpi=1200, bbox_inches="tight")
plt.show()

