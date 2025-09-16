import matplotlib.pyplot as plt
import numpy as np
import time

# Intercept (c) fixed
c = 0

# Generate x values
x = np.linspace(-10, 10, 200)

plt.ion()  # turn on interactive mode

for angle in range(0, 181, 1):  # rotate slope from 0° to 180°
    m = np.tan(np.radians(angle))  # slope from angle
    y = m * x + c

    plt.clf()  # clear previous plot
    plt.plot(x, y, label=f"Angle: {angle}°, y = {round(m,2)}x + {c}")
    plt.axhline(0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(0, color='black', linewidth=0.5)  # y-axis
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Rotating Line (y = mx + c)")
    plt.legend()
    plt.grid(True)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.draw()
    plt.pause(0.2)  # small delay (in seconds)

plt.ioff()  # turn off interactive mode
plt.show()
