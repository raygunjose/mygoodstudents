import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis


plt.grid(True)

plt.xlim(-20, 20)   # X-axis from -1 to 3
plt.ylim(-20, 20)   # Y-axis from -1 to 3

# Add labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.title("Graph of y = mx + c")

# Equation parameters
m = 0.5   # slope
c = 5   # intercept

# Generate x values
x = np.linspace(-10, 5, 3)  # from -10 to 10 with 100 points
y = m * x + c  # y = mx + c

# Plot the line
plt.plot(x, y, label=f"y = {m}x + {c}")
plt.scatter(x, y, color="red", s=20, label="Points")
plt.legend()
# Show the graph
plt.show()
