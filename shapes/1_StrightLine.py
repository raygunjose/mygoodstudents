import matplotlib.pyplot as plt

# Coordinates for the line
x = [0, 2]
y = [0, 2]

# Plot the line
plt.plot(x, y, label="Line y=x", color="blue")

# Add labels and grid
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line")
plt.legend()
plt.grid(True)

# Set axis limits
plt.xlim(-1, 3)   # X-axis from -1 to 3
plt.ylim(-1, 3)   # Y-axis from -1 to 3

# Show the graph
plt.show()
