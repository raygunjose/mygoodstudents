import matplotlib.pyplot as plt
import time

# Set up the figure
plt.ion()  # turn on interactive mode
fig, ax = plt.subplots()

x = [0, 2]

for slope in range(1, 6):  # slope goes 1, 2, 3, 4, 5
    y = [0, slope * 2]  # y increases with slope

    ax.clear()
    ax.plot(x, y, color="blue", label=f"Slope = {slope}")
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 10)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Line with Increasing Slope")
    ax.legend()
    ax.grid(True)

    plt.draw()
    plt.pause(0.5)  # short delay (in seconds)

plt.ioff()
plt.show()
