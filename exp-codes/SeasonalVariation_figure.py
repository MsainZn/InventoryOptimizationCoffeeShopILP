
import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend('TkAgg')

# Data for product prices
product_prices = [
    168.7896, 70.94304, 190.12392, 151.13952, 67.473, 104.6724, 26.01816, 39.7341,
    197.74944, 17.80002, 11.00988, 92.43648, 50.35536, 24.28416, 10.62432, 25.602,
    5.3856, 320.4537468, 243.27075735, 185.90026575, 195.994224, 314.9420544,
    465.26335335, 357.41412, 136.239768, 42.66864, 254.93472, 127.34496, 197.705376,
    64.418508, 175.487328, 7.033716, 11.619585, 13.84803, 82.79442, 50.49765, 63.82395,
    13.69809, 28.83438, 30.51126
]

# Seasonal coefficients for each product by month
seasonal_coefficients = {
    "Espresso": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Americano": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3],
    "Latte": [1.4, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Cappuccino": [1.4, 1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Macchiato": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Mocha": [1.4, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Flat white": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Affogato": [1.0, 1.1, 1.1, 1.2, 1.3, 1.4, 1.4, 1.5, 1.3, 1.2, 1.1, 1.0],
    "Caramel macchiato": [1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Misto": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 0.8, 1.0, 1.1, 1.2, 1.3],
    "Cortado": [1.3, 1.2, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Black tea": [1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 0.8, 1.0, 1.1, 1.2, 1.3],
    "Green tea": [1.1, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.1, 1.0, 1.0, 1.1],
    "Sour tea": [1.1, 1.1, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.1, 1.0, 1.0, 1.1],
    "Mint tea": [1.1, 1.1, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.1, 1.0, 1.0, 1.1],
    "Earl grey tea": [1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 0.9, 1.0, 1.1, 1.2, 1.3],
    "Ginger tea": [1.4, 1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Chocolate cake": [1.1, 1.0, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 1.2],
    "Lemon cake": [1.0, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.4, 1.2, 1.1, 1.0, 1.0],
    "Carrot cake": [1.1, 1.1, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 1.2],
    "Strawberry cake": [1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.5, 1.3, 1.2, 1.1, 1.0],
    "Red velvet cake": [1.1, 1.1, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 1.3],
    "Cheesecake": [1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.4, 1.4, 1.2, 1.1, 1.0, 1.0],
    "Chocolate milkshake": [1.0, 0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.5, 1.3, 1.2, 1.1, 1.0],
    "Vanilla milkshake": [0.9, 0.9, 1.0, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.0, 0.9],
    "Coffee milkshake": [1.0, 1.0, 1.0, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.1, 1.0],
    "Strawberry milkshake": [0.8, 0.7, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Banana milkshake": [0.9, 0.8, 0.9, 1.0, 1.2, 1.4, 1.5, 1.5, 1.3, 1.2, 1.1, 0.9],
    "Strawberry banana smoothie": [0.7, 0.6, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Chocolate banana smoothie": [0.8, 0.6, 0.9, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.1, 1.0],
    "Mango smoothie": [0.8, 0.8, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Peanut butter banana smoothie": [0.9, 0.8, 0.9, 1.0, 1.2, 1.4, 1.4, 1.4, 1.2, 1.1, 1.0, 0.9],
    "Ice tea": [0.7, 0.6, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Ice coffee": [0.7, 0.6, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Lemonade": [0.6, 0.5, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Mojito": [0.7, 0.7, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Ferappaccino": [0.7, 0.7, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Honey & milk": [1.2, 1.2, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.3, 1.3],
    "Hot chocolate": [1.4, 1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Chocolate milk": [1.2, 1.1, 1.2, 1.1, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.3, 1.3]
}
# Define product categories
COLD_DRINKS = {
    "Ice tea", "Ice coffee", "Lemonade", "Mojito", "Ferappaccino", "Chocolate milkshake",
    "Vanilla milkshake", "Coffee milkshake", "Strawberry milkshake", "Banana milkshake",
    "Strawberry banana smoothie", "Chocolate banana smoothie", "Mango smoothie",
    "Peanut butter banana smoothie"
}
HOT_DRINKS = {
    "Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat white",
    "Affogato", "Caramel macchiato", "Misto", "Cortado", "Black tea", "Green tea",
    "Sour tea", "Mint tea", "Earl grey tea", "Ginger tea", "Honey & milk", "Hot chocolate",
    "Chocolate milk"
}
CAKES = {
    "Chocolate cake", "Lemon cake", "Carrot cake", "Strawberry cake", "Red velvet cake", "Cheesecake"
}

# Initialize arrays for profit calculations
MONTHS = np.arange(12)
total_profits = np.zeros(12)
category_profits = {
    "Hot Drinks": np.zeros(12),
    "Cold Drinks": np.zeros(12),
    "Cakes": np.zeros(12)
}

# Calculate profits for each product and accumulate by category
for product, price in zip(seasonal_coefficients.keys(), product_prices):
    monthly_profits = price * np.array(seasonal_coefficients[product])
    total_profits += monthly_profits

    if product in HOT_DRINKS:
        category_profits["Hot Drinks"] += monthly_profits
    elif product in COLD_DRINKS:
        category_profits["Cold Drinks"] += monthly_profits
    elif product in CAKES:
        category_profits["Cakes"] += monthly_profits

# Define inventory cost and net profits
INVENTORY_COST = 1965.1
net_profits = total_profits - INVENTORY_COST

# Plotting net profits by category (Hot Drinks, Cold Drinks, Cakes)
#plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(figsize=(14, 8))

# Plot stacked bars for each category
ax.bar(MONTHS + 1, category_profits["Hot Drinks"] - INVENTORY_COST / 3, color='#FF9999', label='Hot Drinks')
ax.bar(
    MONTHS + 1,
    category_profits["Cold Drinks"] - INVENTORY_COST / 3,
    color='#99CCFF',
    label='Cold Drinks',
    bottom=category_profits["Hot Drinks"] - INVENTORY_COST / 3
)
ax.bar(
    MONTHS + 1,
    category_profits["Cakes"] - INVENTORY_COST / 3,
    color='forestgreen',
    label='Cakes',
    bottom=category_profits["Hot Drinks"] + category_profits["Cold Drinks"] - 2 * INVENTORY_COST / 3
)

# Set x-axis labels
month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticks(MONTHS + 1)
ax.set_xticklabels(month_labels, rotation=45, fontsize=16)

# Set y-tick labels font size
ax.tick_params(axis='y', labelsize=16)


# Set labels and legend
ax.set_xlabel('Month', fontsize=18)
ax.set_ylabel('Gross Profit ($)', fontsize=18)
ax.legend(loc='upper left', fontsize=14)
#ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.grid(False)

# Optimize layout and show plot
plt.tight_layout()
plt.show()
#plt.savefig('Seasonalvariation_Figure20.png', format='png', dpi=300)
