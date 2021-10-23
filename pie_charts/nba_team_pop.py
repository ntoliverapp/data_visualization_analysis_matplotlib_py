import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Team Popularity
labels = ['Lakers', 'Warriors', 'Hawks', 'Celtics', 'Suns', ]
popularity = [59219, 55466, 36443, 35917, 31991]
colors= ['#FDB927', '#5D76A9', '#E03A3E', '#007A33', '#E56020']
explode= [0.1, 0, 0, 0, 0]

plt.pie(popularity, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%')

plt.title('NBA Teams')

plt.tight_layout()

plt.

plt.show()