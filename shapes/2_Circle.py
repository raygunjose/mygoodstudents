import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Draw a circle (center = (0,0), radius = 1)
circle = plt.Circle((0, 0), 1, color="skyblue", ec="black")
ax.add_patch(circle)

# Set equal aspect ratio so circle doesn’t look like an oval
ax.set_aspect("equal")

# Set axis limits
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# Add grid and labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Circle")
plt.grid(True)

plt.show()
