import matplotlib.pyplot as plt
import time

plt.ion()  # interactive mode
fig, ax = plt.subplots()

# Center of circle
xc, yc = 0, 0

# Loop for radius increase
for r in range(1, 11):  # radius from 1 to 10
    ax.clear()
    circle = plt.Circle((xc, yc), r, fill=False, color="blue", linewidth=2)
    ax.add_patch(circle)
    
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect("equal")
    ax.set_title(f"Circle with Radius = {r}")
    ax.grid(True)

    plt.draw()
    plt.pause(0.5)  # 0.5 sec delay

plt.ioff()
plt.show()
