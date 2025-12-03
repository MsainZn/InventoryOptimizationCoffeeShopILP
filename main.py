
import json
from docplex.mp.model import Model

# Load the dataset from JSON file
with open('Dataset.json', 'r') as f:
    data = json.load(f)

products = data['products']
N = len(products)  # Number of products

# Collect unique ingredients in order of first appearance
ing_to_idx = {}
ing_list = []
buying_prices = {}
buying_units = {}
for prod in products:
    for ing in prod['ingredients']:
        name = ing['name']
        if name not in ing_to_idx:
            ing_to_idx[name] = len(ing_list)
            ing_list.append(name)
            buying_prices[name] = ing['buying_price']
            buying_units[name] = ing['buying_unit']

M = len(ing_list)  # Number of unique ingredients

# Sell prices
sell_prices = [prod['sell_price'] for prod in products]

# Minimum sale ratios from February (convert % to decimal)
min_ratios = [float(prod['sale_ratio']['February'].rstrip('%')) / 100 for prod in products]

# Usage matrix: usage[i][j] = quantity used per product i for ingredient j, normalized by buying_unit
usage = [[0.0] * M for _ in range(N)]
for i, prod in enumerate(products):
    for ing in prod['ingredients']:
        name = ing['name']
        j = ing_to_idx[name]
        qty = ing['quantity_usedIn_product_per_buying_unit']
        usage[i][j] = qty / buying_units[name]

# Inflated prices dict
inflated = {
    "Espresso beans": 20.4,
    "Milk": 1.6,
    "Water": 0.6,
    "Dried hibiscus flowers": 25.2,
    "Cream": 1.7,
    "Chocolate syrup": 16.9,
    "Baking soda": 9.5,
    "Black tea loose leaf": 7.6,
    "Green tea loose leaf": 8.2,
    "Dried mint leaf": 5.7,
    "Dried ginger root": 1.4,
    "Honey": 2.2,
    "Ground cinnamon": 7.3,
    "Graham cracker crumbs": 12.8,
    "All-purpose flour": 6.9,
    "Sugar": 1.4,
    "Salt": 0.6,
    "Cocoa powder": 15.3,
    "Baking powder": 1.00,
    "Eggs": 3.47,
    "Butter": 2.4,
    "Vanilla extract": 16.6,
    "Ground ginger": 10.2,
    "Lemon juice": 2.3,
    "Vegetable oil": 2.7,
    "Grated carrots": 0.5,
    "Cream cheese": 1.8,
    "Ice-cream": 5.6,
    "Strawberries": 8.2,
    "Yogurt": 2.6,
    "Caramel sauce": 13.2,
    "Peanut butter": 10.5,
    "Mango": 5.30,
    "Banana": 1.22
}

# ALPHA list by category
ALPHA_list = [3.5] * 11 + [8] * 6 + [2.3] * 6 + [2.4] * 5 + [2.4] * 4 + [1.5] * 8

# Purchase discount coefficient
BETA = 0.85

# Create the model
model = Model(name='Menu Optimization')

# Variables for number of each product 
p = model.integer_var_list(N, lb=0, name='p')

# Variables for number of packages of each ingredient
x = model.integer_var_list(M, lb=0, name='x')

# Objective: Maximize revenue - original inventory cost
obj = model.sum(sell_prices[i] * p[i] for i in range(N)) - model.sum(buying_prices[ing_list[j]] * x[j] for j in range(M))
model.maximize(obj)

# Constraints for ingredient usages
for j in range(M):
    model.add_constraint(model.sum(usage[i][j] * p[i] for i in range(N)) <= x[j], ctname=f'c{j+1}')

# Constraints for sales distribution (minimum ratios)
total_sales = model.sum(p)
for i in range(N):
    model.add_constraint(p[i] >= min_ratios[i] * total_sales, ctname=f'c{M + i + 1}')

# Budget constraint using adjusted (inflated * BETA) prices
budget_expr = model.sum(inflated[ing_list[j]] * BETA * x[j] for j in range(M))
model.add_constraint(budget_expr <= 2500, ctname=f'c{M + N + 1}')

# Solve the model
solution = model.solve()

# Output the solution
print(solution)
print('---------------------------')

if solution:
    # Get values
    p_values = [solution.get_value(p[i]) for i in range(N)]
    x_values = [solution.get_value(x[j]) for j in range(M)]

    # Inventory cost using adjusted prices
    InventoryCost = sum(inflated[ing_list[j]] * BETA * x_values[j] for j in range(M))

    # Compute ip_price (adjusted cost per product)
    ip_prices = []
    for i in range(N):
        ip_price = sum(usage[i][j] * inflated[ing_list[j]] * BETA for j in range(M))
        ip_prices.append(ip_price)

    # Compute Op_price = ip_price * ALPHA
    Op_prices = [ip_prices[i] * ALPHA_list[i] for i in range(N)]

    # Total selling price (Gross Profit)
    GrossProfit = sum(Op_prices[i] * p_values[i] for i in range(N))

    # Net Profit
    NetProfit = GrossProfit - InventoryCost
  
    print(f'GrossProfit: {GrossProfit}')
    print(f'InventoryCost: {InventoryCost}')
    print(f'NetProfit: {NetProfit}')
    # The difference between the price of net profit, Gross profit and the price of objective function is because the production price of the product in the objective function has been rounded up.
    print('---------------------------')
else:
    print("No solution found.")
