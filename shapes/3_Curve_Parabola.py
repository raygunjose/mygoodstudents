import matplotlib.pyplot as plt
import numpy as np

# X values from -5 to 5
x = np.linspace(-5, 5, 200)
y = x**2  # parabola curve

plt.plot(x, y, color="green", linewidth=2, label="y = x²")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Curve (Parabola)")
plt.legend()
plt.grid(True)
plt.show()
