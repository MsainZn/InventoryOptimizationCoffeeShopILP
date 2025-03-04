import matplotlib.pyplot as plt
import numpy as np

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

categories = {
   "Smoothies": ["Strawberry banana smoothie", "Chocolate banana smoothie", "Mango smoothie", "Peanut butter banana smoothie"],
   "Milkshakes": ["Chocolate milkshake", "Vanilla milkshake", "Coffee milkshake", "Strawberry milkshake", "Banana milkshake"],
    "Cakes": ["Chocolate cake", "Lemon cake", "Carrot cake", "Strawberry cake", "Red velvet cake", "Cheesecake"],
    "Others": ["Honey & milk", "Hot chocolate", "Chocolate milk","Ice tea", "Ice coffee", "Lemonade", "Mojito", "Frappuccino"],
    "Tea": ["Black tea", "Green tea", "Sour tea", "Mint tea", "Earl grey tea", "Ginger tea"],
    "Coffee": ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat white", "Affogato", "Caramel macchiato", "Misto", "Cortado"],
}

# Calculate the total values for each category
category_values = {}
for category, items in categories.items():
    category_values[category] = sum(product_values[product_names.index(item)] for item in items)

# Extract labels and values for the pie chart
labels = list(category_values.keys())
values = list(category_values.values())

# Define the color gradient using a colormap
colors = plt.cm.Greens(np.linspace(0.1, 0.4, len(labels)))  # Adjusted for a single gradient color (Blues)

# Create the pie chart with a single gradient color scheme
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, 
        colors=colors, textprops={'fontsize': 16}, 
        wedgeprops={'edgecolor': 'white', 'linewidth': 0.5})  # Lighter borders for cleaner look

# Title and layout
#plt.title('Sale Distribution by Menu Item Categories', fontsize=14)
plt.tight_layout()

# Display the pie chart
plt.show()
#plt.savefig("sale_distribution_final.png", format='png',dpi=300, bbox_inches="tight")

