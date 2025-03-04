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

# Optimum numbers for each ingredient in budget in y-axis
butter_1700 = 27
butter_2400 = 41
butter_3100 = 54
butter_3800 = 68
butter_4500 = 80
butter = [butter_1700, butter_2400, butter_3100, butter_3800, butter_4500]
butter_1 = [butter_1700, butter_1700, butter_1700, butter_1700, butter_1700, butter_1700, butter_1700, butter_2400,
            butter_2400, butter_2400, butter_2400, butter_2400, butter_2400, butter_2400, butter_3100, butter_3100,
            butter_3100, butter_3100, butter_3100, butter_3100, butter_3100, butter_3800, butter_3800, butter_3800,
            butter_3800, butter_3800, butter_3800, butter_3800, butter_4500]

sugar_1700 = 21
sugar_2400 = 32
sugar_3100 = 42
sugar_3800 = 52
sugar_4500 = 63
sugar = [sugar_1700, sugar_2400, sugar_3100, sugar_3800, sugar_4500]
sugar_1 = [sugar_1700, sugar_1700, sugar_1700, sugar_1700, sugar_1700, sugar_1700, sugar_1700, sugar_2400, sugar_2400,
           sugar_2400, sugar_2400, sugar_2400, sugar_2400, sugar_2400, sugar_3100, sugar_3100, sugar_3100, sugar_3100,
           sugar_3100, sugar_3100, sugar_3100, sugar_3800, sugar_3800, sugar_3800, sugar_3800, sugar_3800, sugar_3800,
           sugar_3800, sugar_4500]

icecream_1700 = 14
icecream_2400 = 21
icecream_3100 = 28
icecream_3800 = 35
icecream_4500 = 42
icecream = [icecream_1700, icecream_2400, icecream_3100, icecream_3800, icecream_4500]
icecream_1 = [icecream_1700, icecream_1700, icecream_1700, icecream_1700, icecream_1700, icecream_1700, icecream_1700,
              icecream_2400, icecream_2400, icecream_2400, icecream_2400, icecream_2400, icecream_2400, icecream_2400,
              icecream_3100, icecream_3100, icecream_3100, icecream_3100, icecream_3100, icecream_3100, icecream_3100,
              icecream_3800, icecream_3800, icecream_3800, icecream_3800, icecream_3800, icecream_3800, icecream_3800,
              icecream_4500]

espresso_beans_1700 = 8
espresso_beans_2400 = 12
espresso_beans_3100 = 16
espresso_beans_3800 = 20
espresso_beans_4500 = 23
espresso_beans = [espresso_beans_1700, espresso_beans_2400, espresso_beans_3100, espresso_beans_3800,
                  espresso_beans_4500]
espresso_beans_1 = [espresso_beans_1700, espresso_beans_1700, espresso_beans_1700, espresso_beans_1700,
                    espresso_beans_1700,
                    espresso_beans_1700, espresso_beans_1700, espresso_beans_2400, espresso_beans_2400,
                    espresso_beans_2400,
                    espresso_beans_2400, espresso_beans_2400, espresso_beans_2400, espresso_beans_2400,
                    espresso_beans_3100,
                    espresso_beans_3100, espresso_beans_3100, espresso_beans_3100, espresso_beans_3100,
                    espresso_beans_3100,
                    espresso_beans_3100, espresso_beans_3800, espresso_beans_3800, espresso_beans_3800,
                    espresso_beans_3800,
                    espresso_beans_3800, espresso_beans_3800, espresso_beans_3800, espresso_beans_4500]

salt_1700 = 6
salt_2400 = 8
salt_3100 = 11
salt_3800 = 14
salt_4500 = 16
salt = [salt_1700, salt_2400, salt_3100, salt_3800, salt_4500]
salt_1 = [salt_1700, salt_1700, salt_1700, salt_1700, salt_1700, salt_1700, salt_1700, salt_2400, salt_2400, salt_2400,
          salt_2400,
          salt_2400, salt_2400, salt_2400, salt_3100, salt_3100, salt_3100, salt_3100, salt_3100, salt_3100, salt_3100,
          salt_3800,
          salt_3800, salt_3800, salt_3800, salt_3800, salt_3800, salt_3800, salt_4500]

# Plot setup
fig, ax = plt.subplots(figsize=(6, 8))
fig.patch.set_facecolor('white')

# plot data
ax.plot(budget, espresso_beans, '--o', c='royalblue', linewidth=2)
ax.plot(budget, sugar, '--o', c='forestgreen', linewidth=2)
ax.plot(budget, salt, '--o', c='orange', linewidth=2)
ax.plot(budget, butter, '--o', c='darkslategray', linewidth=2)
ax.plot(budget, icecream, '--o', c='tomato', linewidth=2)

ax.plot(budget_1, butter_1, label='Butter', c='darkslategray', linewidth=1.5)
ax.plot(budget_1, sugar_1, label='Sugar', c='forestgreen', linewidth=1.5)
ax.plot(budget_1, icecream_1, label='Ice-cream', c="tomato", linewidth=1.5)
ax.plot(budget_1, espresso_beans_1, label='Espresso Beans', c='royalblue', linewidth=1.5)
ax.plot(budget_1, salt_1, label='Salt', c='orange', linewidth=1.5)

# Set axes and labels
ax.set_xlabel('Purchasing Budget ($)', fontsize=16)
ax.set_ylabel('Optimum Number of Ingredients', fontsize=16, labelpad=10)

ax.set_ylim(0, 85)
ax.set_xlim(1000, 5500)

# Format ticks
ax.tick_params(axis='both', which='major', labelsize=15, width=1, length=6, color='black')
ax.tick_params(axis='both', which='minor', labelsize=15, width=1, length=3, color='black')

ax.xaxis.set_major_locator(LinearLocator(numticks=6))
ax.yaxis.set_major_locator(LinearLocator(numticks=6))

# Add legend
ax.legend(fontsize=14, loc='upper left', frameon=False, labelspacing=0.4)
ax.minorticks_on()

#plt.savefig('Ingredients_figure.png', format='png', dpi=600)
plt.show()
