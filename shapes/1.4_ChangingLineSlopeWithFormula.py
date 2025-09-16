import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # interactive mode
fig, ax = plt.subplots()

x = np.linspace(0, 5, 100)  # x values from 0 to 5
c = 1  # y-intercept

for m in range(1, 6):  # slope = 1, 2, 3, 4, 5
    y = m * x + c  # formula y = mx + c

    ax.clear()
    ax.plot(x, y, color="blue", label=f"y = {m}x + {c}")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 30)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Line with Changing Slope (y=mx+c)")
    ax.legend()
    ax.grid(True)

    plt.draw()
    plt.pause(0.7)  # 0.7 sec delay

plt.ioff()
plt.show()
