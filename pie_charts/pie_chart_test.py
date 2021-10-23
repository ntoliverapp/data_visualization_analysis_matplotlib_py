import matplotlib.pyplot as plt 

# print(plt.style.available)
plt.style.use('dark_background')

plt.title('Pie Chart Slices')

slices = [50,20,20, 10]
labels = ['Fifty', 'Twenty', 'Twenty', 'Ten']
colors = ['orange', 'green', 'white', 'blue']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'white'})


plt.tight_layout()

plt.savefig('pie_chart_test.png')

plt.show()