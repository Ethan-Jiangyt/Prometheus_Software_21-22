import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import *
import os

plt.style.use(THEME)

# Window positioning
fig, ax = plt.subplots()
fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
fig.set_figheight(FIG_HEIGHT)
fig.set_figwidth(FIG_WIDTH)

filename = max([f for f in os.scandir("logs")], key=lambda x: x.stat().st_mtime).name

def animate(i):
    data = pd.read_csv('logs/' + filename)
    x = data['time'][-NUM_DATA_POINTS:]
    y1 = data['PT1'][-NUM_DATA_POINTS:]
    y2 = data['PT2'][-NUM_DATA_POINTS:]
    y3 = data['PT3'][-NUM_DATA_POINTS:]
    y4 = data['PT4'][-NUM_DATA_POINTS:]

    plt.cla()

    plt.plot(x, y1, label='PT1')
    plt.plot(x, y2, label='PT2')
    plt.plot(x, y3, label='PT3')
    plt.plot(x, y4, label='PT4')
    plt.title('Pressure Transducers')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=REFRESH_RATE)

plt.tight_layout()
plt.show()