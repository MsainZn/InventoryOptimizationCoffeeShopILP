import json
import matplotlib.pyplot as plt
import numpy as np
# Load the JSON data
with open('Full_Dataset.json', 'r') as file:
    data = json.load(file)

# Extract products
data_products = data['products']

# Assume a total sales volume (e.g., 1000 units sold in total)
total_sales_volume = 1159

# Seasonal coefficients for each product (assuming this dictionary is provided as given)
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
    "Red Velvet cake": [1.1, 1.1, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.1, 1.2, 1.3],
    "Cheesecake": [1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.4, 1.4, 1.2, 1.1, 1.0, 1.0],
    "Chocolate milkshake": [1.0, 0.8, 1.0, 1.1, 1.2, 1.4, 1.5, 1.5, 1.3, 1.2, 1.1, 1.0],
    "Vanilla milkshake": [0.9, 0.9, 1.0, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.0, 0.9],
    "Coffee milkshake": [1.0, 1.0, 1.0, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.1, 1.0],
    "Strawberry milkshake": [0.8, 0.7, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Banana milkshake": [0.9, 0.8, 0.9, 1.0, 1.2, 1.4, 1.5, 1.5, 1.3, 1.2, 1.1, 0.9],
    "Strawberry banana smoothie": [0.7, 0.6, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Chocolate banana smoothie": [0.8, 0.6, 0.9, 1.0, 1.1, 1.3, 1.4, 1.4, 1.2, 1.1, 1.1, 1.0],
    "Mango smoothie": [0.8, 0.8, 0.9, 1.0, 1.3, 1.5, 1.6, 1.6, 1.3, 1.2, 1.0, 0.9],
    "Peanut (butter) banana smoothie": [0.9, 0.8, 0.9, 1.0, 1.2, 1.4, 1.4, 1.4, 1.2, 1.1, 1.0, 0.9],
    "Ice tea": [0.7, 0.6, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Ice coffee": [0.7, 0.6, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Lemonade": [0.6, 0.5, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Mojito": [0.7, 0.7, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Frappuccino": [0.7, 0.7, 0.8, 1.0, 1.3, 1.6, 1.7, 1.7, 1.4, 1.1, 0.9, 0.8],
    "Honey & Milk": [1.2, 1.2, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.3, 1.3],
    "Hot chocolate": [1.4, 1.3, 1.3, 1.2, 1.1, 1.0, 0.9, 0.9, 1.0, 1.1, 1.3, 1.4],
    "Chocolate Milk": [1.2, 1.1, 1.2, 1.1, 1.0, 1.0, 1.0, 1.0, 1.2, 1.2, 1.3, 1.3]
}

data_products = [product for product in data_products if 'cake' not in product['name'].lower()]

# Calculate profits for cold month (December, index 11) and hot month (July, index 6)
product_names = []
profit_values_cold = []
profit_values_hot = []

for product in data_products:
    name = product['name']
    sell_price = product['sell_price']
    rounded_cost = product['rounded_cost']
    sale_ratio = float(product['sale_ratio'].strip('%')) / 100
    product_sales_volume = sale_ratio * total_sales_volume

    # Seasonal adjustment
    seasonal_cold = seasonal_coefficients[name][11]  # December
    seasonal_hot = seasonal_coefficients[name][6]   # July

    # Adjust sales volumes
    adjusted_sales_volume_cold = product_sales_volume * seasonal_cold
    adjusted_sales_volume_hot = product_sales_volume * seasonal_hot

    # Calculate profits for cold and hot months
    total_profit_cold = (sell_price - rounded_cost) * adjusted_sales_volume_cold
    total_profit_hot = (sell_price - rounded_cost) * adjusted_sales_volume_hot

    # Append data in original order
    product_names.append(name)
    profit_values_cold.append(total_profit_cold)
    profit_values_hot.append(total_profit_hot)

# Plotting the data
plt.figure(figsize=(14, 8))
x = np.arange(len(product_names))

plt.plot(x, profit_values_cold, label='December', color='royalblue', linewidth=1.7)
plt.plot(x, profit_values_hot, label='July', color='tomato', linewidth=1.7)

# Adding labels and title
plt.xticks(x, product_names, rotation=90, fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel('Gross Profits ($)',fontsize=18)
plt.xlabel('Products',fontsize=18)
#plt.title('Cold vs Hot Month Profits for Products (Original Order)')

# Adding legend
plt.legend(frameon=False,fontsize=16)

# Adjust layout for better visibility of labels
plt.tight_layout()

# Show the plot
plt.show()
#plt.savefig('most_profitable3.png', format='png', dpi=250)

#print(sum(profit_values_hot))
#print(sum(profit_values_cold))