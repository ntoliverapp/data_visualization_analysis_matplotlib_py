import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Team Popularity
labels = ['Lakers', 'Warriors', 'Nets', 'Celtics', 'Suns', ]

popularity = [59219, 55466, 36443, 35917, 31991]

colors= ['#552583', '#1D428A', 'black', '#007A33', '#E56020']

plt.pie(popularity, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

plt.title('NBA Teams')

plt.tight_layout()

plt.show()