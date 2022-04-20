import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import *
import os

plt.style.use(THEME)

# Window positioning
fig, ax = plt.subplots()
fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 1080*(0.5)))
fig.set_figheight(FIG_HEIGHT)
fig.set_figwidth(FIG_WIDTH)


filename = max([f for f in os.scandir("logs")], key=lambda x: x.stat().st_mtime).name

def animate(i):
    data = pd.read_csv('logs/' + filename)
    x = data['time'][-NUM_DATA_POINTS:]
    # y1 = data['total_1'][-100:]
    y2 = data['LC'][-NUM_DATA_POINTS:]

    plt.cla()

    # plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='LC')
    plt.title('Load Cell')
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=40)

plt.tight_layout()
plt.show()