import matplotlib.pyplot as plt
import numpy as np

# Radius of the circle
r = 1  

# Theta values (0 to 2π)
theta = np.linspace(0, 2*np.pi, 500)

# Parametric equations of the circle
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the circle
plt.plot(x, y, color="red", label="x² + y² = r²")

# Axis settings
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Circle using Formula (x² + y² = r²)")
plt.legend()
plt.grid(True)
plt.gca().set_aspect("equal")  # Keep aspect ratio equal

# Set axis limits
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()
