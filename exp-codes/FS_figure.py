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
            3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500]  # steps lines in x-axis

# Optimum prices for each price in budget in y-axis

gross_1700 = 3117.6
gross_2400 = 4676.4
gross_3100 = 6235.2
gross_3800 = 7794.0
gross_4500 = 9352.8
gross = [gross_1700, gross_2400, gross_3100, gross_3800, gross_4500]
gross_1 = [gross_1700, gross_1700, gross_1700, gross_1700, gross_1700, gross_1700, gross_1700,
           gross_2400, gross_2400, gross_2400, gross_2400, gross_2400, gross_2400, gross_2400,
           gross_3100, gross_3100, gross_3100, gross_3100, gross_3100, gross_3100, gross_3100,
           gross_3800, gross_3800, gross_3800, gross_3800, gross_3800, gross_3800, gross_3800,
           gross_4500]

cost_1700 = 1356.8
cost_2400 = 1976.3
cost_3100 = 2586.4
cost_3800 = 3215.6
cost_4500 = 3814.8
cost = [cost_1700, cost_2400, cost_3100, cost_3800, cost_4500]
cost_1 = [cost_1700, cost_1700, cost_1700, cost_1700, cost_1700, cost_1700, cost_1700,
          cost_2400, cost_2400, cost_2400, cost_2400, cost_2400, cost_2400, cost_2400,
          cost_3100, cost_3100, cost_3100, cost_3100, cost_3100, cost_3100, cost_3100,
          cost_3800, cost_3800, cost_3800, cost_3800, cost_3800, cost_3800, cost_3800,
          cost_4500]

net_1700 = 1760.7
net_2400 = 2700.0
net_3100 = 3648.7
net_3800 = 4578.3
net_4500 = 5537.9
net = [net_1700, net_2400, net_3100, net_3800, net_4500]
net_1 = [net_1700, net_1700, net_1700, net_1700, net_1700, net_1700, net_1700,
         net_2400, net_2400, net_2400, net_2400, net_2400, net_2400, net_2400,
         net_3100, net_3100, net_3100, net_3100, net_3100, net_3100, net_3100,
         net_3800, net_3800, net_3800, net_3800, net_3800, net_3800, net_3800,
         net_4500]

# Plot setup
fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor('white')

# Plot data
ax.plot(budget, gross,'--o',c='forestgreen', linewidth=1.5)
ax.plot(budget, net, '--o',c='royalblue', linewidth=1.5)
ax.plot(budget, cost, '--o', c='tomato', linewidth=1.5)

ax.plot(budget_1, gross_1, label='Sale Revenue',c='forestgreen',linewidth=1.5)
ax.plot(budget_1, net_1, label='Gross Profit', c='royalblue', linewidth=1.5)
ax.plot(budget_1, cost_1, label='Inventory Cost', c='tomato', linewidth=1.5)

# Set axes and labels
ax.set_xlabel('Budget ($)', fontsize=18)
ax.set_ylabel('Price ($)', fontsize=18)

ax.set_ylim(500, 10000)
ax.set_xlim(1500, 5000)

# Format ticks
ax.tick_params(axis='both', which='major', labelsize=16, width=1, length=6, color='black')
ax.tick_params(axis='both', which='minor', labelsize=16, width=1, length=3, color='black')

ax.xaxis.set_major_locator(LinearLocator(numticks=6))
ax.yaxis.set_major_locator(LinearLocator(numticks=6))

# Add legend
ax.legend(fontsize=16,loc='upper left', frameon=False, labelspacing=0.4)
ax.minorticks_on()

# Adjust subplot layout
fig.subplots_adjust(left=0.15)

#plt.savefig('FS_figure20.png', format='png', dpi=300)
plt.show()
