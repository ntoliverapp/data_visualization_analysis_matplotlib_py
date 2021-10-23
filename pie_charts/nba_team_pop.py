import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Team Popularity
labels = ['Lakers', 'Warriors', 'Nets', 'Celtics', 'Suns', 'Wizards', 'Cavaliers', 'Hornets', 'Bucks', 'Hawks']

popularity = [59219, 55466, 36443, 35917, 31991, 23030, 20524, 18523, 7331,  5833]

colors= ['#552583', '#1D428A', 'black', '#007A33', '#E56020', '#C4CED4', '#FDBB30', '#1D1160', '#00471B', '#E03A3E']

plt.pie(popularity, labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

plt.title('NBA Teams')

plt.tight_layout()

plt.show()