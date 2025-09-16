import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # interactive mode
fig, ax = plt.subplots()

# Original line endpoints
x1, y1 = 0, 0
x2, y2 = 4, 4  # slope = 1 line (y=x)

# Find center of line
xc = (x1 + x2) / 2
yc = (y1 + y2) / 2

# Angles for rotation (0° to 270° in steps)
angles = np.linspace(0, 270, 10)  # 10 steps

for theta in np.deg2rad(angles):  # convert degrees to radians
    # Rotate point 1
    x1r = xc + (x1 - xc) * np.cos(theta) - (y1 - yc) * np.sin(theta)
    y1r = yc + (x1 - xc) * np.sin(theta) + (y1 - yc) * np.cos(theta)

    # Rotate point 2
    x2r = xc + (x2 - xc) * np.cos(theta) - (y2 - yc) * np.sin(theta)
    y2r = yc + (x2 - xc) * np.sin(theta) + (y2 - yc) * np.cos(theta)

    ax.clear()
    ax.plot([x1r, x2r], [y1r, y2r], color="blue", linewidth=2)
    ax.scatter([xc], [yc], color="red", marker="o", label="Center")
    ax.set_xlim(-5, 8)
    ax.set_ylim(-5, 8)
    ax.set_aspect("equal")
    ax.set_title(f"Rotating Line (Angle={int(np.rad2deg(theta))}°)")
    ax.grid(True)
    ax.legend()

    plt.draw()
    plt.pause(0.7)  # delay

plt.ioff()
plt.show()
