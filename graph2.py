import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['time'][-100:]
    y1 = data['TC1'][-100:]
    y2 = data['TC2'][-100:]
    y3 = data['TC3'][-100:]
    y4 = data['TC4'][-100:]

    plt.cla()

    plt.plot(x, y1, label='TC1')
    plt.plot(x, y2, label='TC2')
    plt.plot(x, y3, label='TC3')
    plt.plot(x, y4, label='TC4')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=200)

plt.tight_layout()
plt.show()