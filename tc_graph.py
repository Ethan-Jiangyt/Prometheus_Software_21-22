import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import NUM_DATA_POINTS
import os

plt.style.use('fivethirtyeight')

filename = max([f for f in os.scandir("logs")], key=lambda x: x.stat().st_mtime).name

def animate(i):
    data = pd.read_csv('logs/' + filename)
    x = data['time'][-NUM_DATA_POINTS:]
    y1 = data['TC1'][-NUM_DATA_POINTS:]
    y2 = data['TC2'][-NUM_DATA_POINTS:]
    y3 = data['TC3'][-NUM_DATA_POINTS:]
    y4 = data['TC4'][-NUM_DATA_POINTS:]

    plt.cla()

    plt.plot(x, y1, label='TC1')
    plt.plot(x, y2, label='TC2')
    plt.plot(x, y3, label='TC3')
    plt.plot(x, y4, label='TC4')
    plt.title('Thermocouples')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=40)

plt.tight_layout()
plt.show()