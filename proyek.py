import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Definisi titik-titik pada objek 3D
points = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]

# Definisi wajah-wajah pada objek 3D (urutan titik-titik)
faces = [
    [points[0], points[1], points[2], points[3]],
    [points[4], points[5], points[6], points[7]],
    [points[0], points[1], points[5], points[4]],
    [points[2], points[3], points[7], points[6]],
    [points[1], points[2], points[6], points[5]],
    [points[0], points[3], points[7], points[4]]
]

# Membuat plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Menambahkan wajah-wajah objek 3D ke plot
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5))

# Menyesuaikan batas sumbu
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Menampilkan plot
plt.show()
