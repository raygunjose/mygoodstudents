import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Face
face = plt.Circle((0.5, 0.5), 0.3, color="peachpuff", ec="black")
ax.add_patch(face)

# Eyes
ax.add_patch(plt.Circle((0.4, 0.6), 0.05, color="white", ec="black"))
ax.add_patch(plt.Circle((0.6, 0.6), 0.05, color="white", ec="black"))
ax.add_patch(plt.Circle((0.4, 0.6), 0.02, color="black"))
ax.add_patch(plt.Circle((0.6, 0.6), 0.02, color="black"))

# Nose (big exaggerated)
ax.add_patch(plt.Circle((0.5, 0.45), 0.08, color="peachpuff", ec="black"))

# Mouth
mouth_x = np.linspace(0.4, 0.6, 100)
mouth_y = 0.35 + 0.02*np.sin(10*mouth_x)
ax.plot(mouth_x, mouth_y, color="red")

# Ears (big exaggerated)
ax.add_patch(plt.Circle((0.18, 0.5), 0.08, color="peachpuff", ec="black"))
ax.add_patch(plt.Circle((0.82, 0.5), 0.08, color="peachpuff", ec="black"))

ax.set_aspect("equal")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.axis("off")
plt.show()
