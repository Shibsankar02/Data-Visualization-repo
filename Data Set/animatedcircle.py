import matplotlib
matplotlib.use("TkAgg")  # Force external window

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# User input
speed = float(input("Enter speed (e.g., 0.05): "))
frames = int(input("Enter number of frames (e.g., 200): "))

# Setup figure
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)
ax.set_title("Moving Circle - Straight Line")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)

# Draw straight reference line (optional)
x = np.linspace(0, 2 * np.pi, 100)
y = np.zeros_like(x)
ax.plot(x, y, linestyle="--")  # straight horizontal line

# Circle
circle = plt.Circle((0, 0), 0.2, color='red')
ax.add_patch(circle)

# Animation function (STRAIGHT LINE)
def animate(frame):
    x_pos = frame * speed
    y_pos = 0  # constant → straight horizontal motion
    circle.set_center((x_pos, y_pos))
    return (circle,)

# Animation
ani = FuncAnimation(
    fig,
    animate,
    frames=frames,
    interval=20,
    blit=True,
    repeat=True
)

# Show
plt.show()