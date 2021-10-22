import matplotlib.pyplot as plt # import library


# list1 = [1,4,5,6,7,9]
# list2 = [9,4,2,1,5,2]

# # 1 - plot a line graph with list1 and name the graph as "Line Graph"
# plt.plot(list1)
# plt.title('Line Graph')

# plt.show()

# # 2 - plot list2 with dot graph( red star), label the point as red star and name the graph as 'Dotted Graph'

# plt.plot(list2, 'r*', )
# plt.legend(loc='best') #add a legend, location is best on the plot
# plt.title('Dotted Graph')

# plt.show()

# #3 - scatterplot using the data below - x-axis as 'a', y-axis as 'b', and color as 's', add labels
# import numpy as np
# data = {
#     'a':np.arange(20),
#     'b':np.random.rand(20),
#     's':np.random.randn(20)
# }
# plt.scatter('a', 'b', c='s', data=data)
# plt.xlabel('x')
# plt.ylabel('y')

# plt.show()
# --------
#5 - Employee Salaries
# Create Create plots comparing employee salaries by age
# Include title, labels, legends
# Fromat the color, marker, line (optional)
# Add grid
# Add style

# print(plt.style.available)
plt.style.use('seaborn-notebook')
# plt.xkcd()

# Median Employee Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

emp_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67137, 68748, 73752]
plt.plot(ages_x, emp_y, color= '#709775', linestyle='--',  marker=',',label='All Employees')

# Median Accountant Salaries by Age
acc_y = [47352, 48567, 53485, 57602, 63023, 65913, 74812, 71585, 71648, 75493, 81573]
plt.plot(ages_x, acc_y, color='#703d57', linestyle='-.', linewidth=2, label='Accountants')

# Median IT Salaries by Age
it_y = [50846, 51856, 52781, 53581, 55035, 59924, 62025, 65829, 67281, 69245, 73857]
plt.plot(ages_x, it_y, color='k', linestyle=':', linewidth=2, label='IT')

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.title('Median Salary (USD) by Age')

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig('salary.png')

plt.show()
