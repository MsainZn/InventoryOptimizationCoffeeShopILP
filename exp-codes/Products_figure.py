# Import matplotlib for plotting
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator

# Set plot style
plt.style.use('classic')
plt.rcParams['font.family'] = 'Times New Roman'

# Data

# Define budgets on x-axis
budget = [1700, 2400, 3100, 3800, 4500]  # trend lines in x-axis
budget_1 = [1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400,
            3500, 3600,3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500]  # steps lines in x-axis

# Optimum numbers for each production in budget in y-axis
americano_1700 = 32
americano_2400 = 48
americano_3100 = 64
americano_3800 = 80
americano_4500 = 96
americano = [americano_1700, americano_2400, americano_3100, americano_3800, americano_4500]
americano_1 = [americano_1700, americano_1700, americano_1700, americano_1700, americano_1700, americano_1700,
               americano_1700,
               americano_2400, americano_2400, americano_2400, americano_2400, americano_2400, americano_2400,
               americano_2400,
               americano_3100, americano_3100, americano_3100, americano_3100, americano_3100, americano_3100,
               americano_3100,
               americano_3800, americano_3800, americano_3800, americano_3800, americano_3800, americano_3800,
               americano_3800,
               americano_4500]

earl_grey_1700 = 10
earl_grey_2400 = 15
earl_grey_3100 = 20
earl_grey_3800 = 25
earl_grey_4500 = 30
earl_grey_tea = [earl_grey_1700, earl_grey_2400, earl_grey_3100, earl_grey_3800, earl_grey_4500]
earl_grey_tea_1 = [earl_grey_1700, earl_grey_1700, earl_grey_1700, earl_grey_1700, earl_grey_1700, earl_grey_1700,
                   earl_grey_1700,
                   earl_grey_2400, earl_grey_2400, earl_grey_2400, earl_grey_2400, earl_grey_2400, earl_grey_2400,
                   earl_grey_2400,
                   earl_grey_3100, earl_grey_3100, earl_grey_3100, earl_grey_3100, earl_grey_3100, earl_grey_3100,
                   earl_grey_3100,
                   earl_grey_3800, earl_grey_3800, earl_grey_3800, earl_grey_3800, earl_grey_3800, earl_grey_3800,
                   earl_grey_3800,
                   earl_grey_4500]

chocolate_cake_1700 = 22
chocolate_cake_2400 = 33
chocolate_cake_3100 = 44
chocolate_cake_3800 = 55
chocolate_cake_4500 = 66
chocolate_cake = [chocolate_cake_1700, chocolate_cake_2400, chocolate_cake_3100, chocolate_cake_3800,
                  chocolate_cake_4500]

chocolate_cake_1 = [chocolate_cake_1700, chocolate_cake_1700, chocolate_cake_1700, chocolate_cake_1700,
                    chocolate_cake_1700, chocolate_cake_1700, chocolate_cake_1700,
                    chocolate_cake_2400, chocolate_cake_2400, chocolate_cake_2400, chocolate_cake_2400,
                    chocolate_cake_2400, chocolate_cake_2400, chocolate_cake_2400,
                    chocolate_cake_3100, chocolate_cake_3100, chocolate_cake_3100, chocolate_cake_3100,
                    chocolate_cake_3100, chocolate_cake_3100, chocolate_cake_3100,
                    chocolate_cake_3800, chocolate_cake_3800, chocolate_cake_3800, chocolate_cake_3800,
                    chocolate_cake_3800, chocolate_cake_3800, chocolate_cake_3800,
                    chocolate_cake_4500]

vanilla_milkshake_1700 = 14
vanilla_milkshake_2400 = 21
vanilla_milkshake_3100 = 28
vanilla_milkshake_3800 = 35
vanilla_milkshake_4500 = 42
vanilla_milkshake = [vanilla_milkshake_1700, vanilla_milkshake_2400, vanilla_milkshake_3100, vanilla_milkshake_3800,
                     vanilla_milkshake_4500]
vanilla_milkshake_1 = [vanilla_milkshake_1700, vanilla_milkshake_1700, vanilla_milkshake_1700, vanilla_milkshake_1700,
                       vanilla_milkshake_1700,
                       vanilla_milkshake_1700, vanilla_milkshake_1700, vanilla_milkshake_2400, vanilla_milkshake_2400,
                       vanilla_milkshake_2400, vanilla_milkshake_2400,
                       vanilla_milkshake_2400, vanilla_milkshake_2400, vanilla_milkshake_2400, vanilla_milkshake_3100,
                       vanilla_milkshake_3100, vanilla_milkshake_3100,
                       vanilla_milkshake_3100, vanilla_milkshake_3100, vanilla_milkshake_3100, vanilla_milkshake_3100,
                       vanilla_milkshake_3800, vanilla_milkshake_3800,
                       vanilla_milkshake_3800, vanilla_milkshake_3800, vanilla_milkshake_3800, vanilla_milkshake_3800,
                       vanilla_milkshake_3800, vanilla_milkshake_4500]

ice_tea_1700 = 6
ice_tea_2400 = 9
ice_tea_3100 = 12
ice_tea_3800 = 15
ice_tea_4500 = 18
ice_tea = [ice_tea_1700, ice_tea_2400, ice_tea_3100, ice_tea_3800, ice_tea_4500]
ice_tea_1 = [ice_tea_1700, ice_tea_1700, ice_tea_1700, ice_tea_1700, ice_tea_1700, ice_tea_1700, ice_tea_1700,
             ice_tea_2400, ice_tea_2400, ice_tea_2400, ice_tea_2400, ice_tea_2400, ice_tea_2400, ice_tea_2400,
             ice_tea_3100, ice_tea_3100, ice_tea_3100, ice_tea_3100, ice_tea_3100, ice_tea_3100, ice_tea_3100,
             ice_tea_3800, ice_tea_3800, ice_tea_3800, ice_tea_3800, ice_tea_3800, ice_tea_3800, ice_tea_3800,
             ice_tea_4500]

# Plot setup
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_facecolor('white')

# plot data
ax.plot(budget, americano, '--o', c='darkslategray', linewidth=2)
ax.plot(budget, chocolate_cake, '--o', c='forestgreen', linewidth=2)
ax.plot(budget, vanilla_milkshake, '--o', c='tomato', linewidth=2)
ax.plot(budget, earl_grey_tea, '--o', c='royalblue', linewidth=2)
ax.plot(budget, ice_tea, '--o', c='orange', linewidth=2)

ax.plot(budget_1, americano_1, c='darkslategray', label='Americano', linewidth=1.5)
ax.plot(budget_1, chocolate_cake_1, c='forestgreen', label='Chocolate Cake', linewidth=1.5)
ax.plot(budget_1, vanilla_milkshake_1, c='tomato', label='Vanilla Milkshake', linewidth=1.5)
ax.plot(budget_1, earl_grey_tea_1, c='royalblue', label='Earl Grey Tea', linewidth=1.5)
ax.plot(budget_1, ice_tea_1, c='orange', label='Ice Tea', linewidth=1.5)

# Set axes and labels
ax.set_xlabel(r'Purchasing Budget ($)', fontsize=16)
ax.set_ylabel('Optimum Number of Products', fontsize=16)

ax.set_ylim(0, 100)
ax.set_xlim(1000, 5500)

# Format ticks
ax.tick_params(axis='both', which='major', labelsize=15, width=1, length=6, color='black')
ax.tick_params(axis='both', which='minor', labelsize=15, width=1, length=3, color='black')

ax.xaxis.set_major_locator(LinearLocator(numticks=6))
ax.yaxis.set_major_locator(LinearLocator(numticks=6))

# Add legend
ax.legend(fontsize=14, loc='upper left', frameon=False, labelspacing=0.4)
ax.minorticks_on()

plt.savefig('Products_figure.png', format='png', dpi=600)
#plt.show()