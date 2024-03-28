from Quaternion import Quaternion
import matplotlib.pyplot as plt
import numpy as np

# Setup a quaternion
v_x = Quaternion(np.array([1, 0, 0, 0]))

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
v_x.plot()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()

# Rotate quaternion

d = 90 # Degrees to rotate around the z-axis
w1 = np.cos(d * np.pi/360)
w2 = np.sin(d * np.pi/360)
v_x_rotated = Quaternion(np.array([w1, 0., 0., 1.*w2]))

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
v_x_rotated.plot()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()
