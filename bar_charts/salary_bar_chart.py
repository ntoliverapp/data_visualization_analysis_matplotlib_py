import matplotlib.pyplot as plt
import numpy as np
# --------
#5 - Employee Salaries
# Create Create bar graphs comparing employee salaries by age, side by side

# print(plt.style.available)
plt.style.use('tableau-colorblind10')

# Median Employee Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

emp_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67137, 68748, 73752]
plt.bar(x_indexes - width, emp_y, width=width, zorder=3,label='All Employees')

# Median Accountant Salaries by Age
acc_y = [47352, 48567, 53485, 57602, 63023, 65913, 74812, 71585, 71648, 75493, 81573]
plt.bar(x_indexes, acc_y, width=width, zorder=3,label='Accountants')

# Median IT Salaries by Age
it_y = [50846, 51856, 52781, 53581, 55035, 59924, 62025, 65829, 67281, 69245, 73857]
plt.bar(x_indexes + width, it_y, width=width, zorder=3, label='IT')

plt.xticks(labels=ages_x, ticks=x_indexes)

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.legend()

plt.grid()

plt.tight_layout()

plt.savefig('salary_bar.png')

plt.show()