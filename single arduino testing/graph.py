import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time'][-100:]
    # y1 = data['total_1'][-100:]
    y2 = data['value'][-100:]

    plt.cla()

    # plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='LC')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=40)

plt.tight_layout()
plt.show()