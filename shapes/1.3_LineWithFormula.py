import matplotlib.pyplot as plt
import numpy as np

# Slope (m) and intercept (c)
m = 1   # slope
c = 0   # y-intercept

# X values
x = np.linspace(-5, 5, 100)

# Line equation y = mx + c
y = m * x + c

# Plot line
plt.plot(x, y, color="blue", label=f"y = {m}x + {c}")

# Axis settings
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line using y = mx + c")
plt.legend()
plt.grid(True)

# Set axis limits
plt.xlim(-6, 6)
plt.ylim(-6, 6)

plt.axhline(0, color="black", linewidth=0.8)  # X-axis
plt.axvline(0, color="black", linewidth=0.8)  # Y-axis

plt.show()
