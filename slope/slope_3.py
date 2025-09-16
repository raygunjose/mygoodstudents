import matplotlib.pyplot as plt
import numpy as np
import time

# Intercept fixed
c = 0  
# Generate x values
x = np.linspace(-10, 10, 200)

# Gradient descent settings
m = 5.0              # initial slope
target_m = 0.0       # final slope (horizontal line)
learning_rate = 0.2  # step size

# Create figure and axis once
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
# ax.axhline(0, color='black', linewidth=0.5)
# ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("Line Rotating with Gradient Descent")
ax.grid(True)

# Initial line object
line, = ax.plot([], [], label="line")
legend = ax.legend()

plt.ion()
plt.show()

for i in range(50):  # max iterations
    # Gradient calculation
    gradient = 2 * (m - target_m)
    m = m - learning_rate * gradient  # update slope

    # Update line data instead of clearing figure
    y = m * x + c
    line.set_data(x, y)
    legend.get_texts()[0].set_text(f"Step {i}, slope={round(m, 3)}")

    fig.canvas.draw()
    fig.canvas.flush_events()

    # Delay slows down as slope gets smaller
    time.sleep(abs(m) * 0.1 + 0.05)

plt.ioff()
plt.show()