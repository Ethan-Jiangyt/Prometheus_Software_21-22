import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time'][-100:]
    y1 = data['PT1'][-100:]
    y2 = data['PT2'][-100:]
    y3 = data['PT3'][-100:]
    y4 = data['PT4'][-100:]

    plt.cla()

    plt.plot(x, y1, label='PT1')
    plt.plot(x, y2, label='PT2')
    plt.plot(x, y3, label='PT3')
    plt.plot(x, y4, label='PT4')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()