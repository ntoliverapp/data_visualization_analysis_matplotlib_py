import matplotlib.pyplot as plt 

# print(plt.style.available)
plt.style.use('dark_background')

plt.title('Pie Chart Slices')

slices = [60,20,20]
labels = ['Sixty', 'Twenty', 'Twenty']

plt.pie(slices, labels=labels)


plt.tight_layout()

plt.show()