from Quaternion import Quaternion
import numpy as np

# Test code
v_x = Quaternion(np.array([1, 0, 0, 0]))
v_y = Quaternion(np.array([0, 0, 1, 0]))
v_z = Quaternion(np.array([0, 0, 0, 1]))

d = 90 # Degrees to rotate around the z-axis

w1 = np.cos(d * np.pi/360)
w2 = np.sin(d * np.pi/360)

q = Quaternion(np.array([w1, 0., 0., 1.*w2]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

v_x.plot()

#for c, v in {'r':v_x, 'g':v_y, 'b':v_z}.items():
#    # Passive rotation
#    q_inv = q ** -1
#    v_new = q * v * q_inv
#    v.plot(color=c, linestyle='-')
#    v_new.plot(color=c, linestyle='-.')

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.legend(['v', 'v new'])