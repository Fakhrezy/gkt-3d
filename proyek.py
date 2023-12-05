import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def affine_transform(points, matrix, translation):
    transformed_points = np.dot(points, matrix.T) + translation
    return transformed_points

def scale_matrix(scaling_factors):
    return np.diag(scaling_factors)

# Titik-titik kubus
points = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# Matriks translasi affine
affine_matrix_translation = np.eye(3)
translation_vector = np.array([2, 2, 0])

# Melakukan translasi affine
transformed_points_translation = affine_transform(points, affine_matrix_translation, translation_vector)

# Matriks skala affine
scaling_factors = np.array([2, 1, 1])
affine_matrix_scale = scale_matrix(scaling_factors)

# Melakukan transformasi skala
transformed_points_scale = affine_transform(points, affine_matrix_scale, np.zeros(3))

# Membuat plot 3D
fig, ax = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})

# Plot untuk translasi
ax[0].set_title('Transformasi Translasi')
transformasi_sebelum_translation = Poly3DCollection([[points[0], points[1], points[2], points[3]],
                                [points[4], points[5], points[6], points[7]],
                                [points[0], points[1], points[5], points[4]],
                                [points[2], points[3], points[7], points[6]],
                                [points[1], points[2], points[6], points[5]],
                                [points[0], points[3], points[7], points[4]]],
                                facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5)
ax[0].add_collection3d(transformasi_sebelum_translation)

# Plot untuk skala
ax[1].set_title('Transformasi Skala')
transformasi_sebelum_scale = Poly3DCollection([[points[0], points[1], points[2], points[3]],
                                [points[4], points[5], points[6], points[7]],
                                [points[0], points[1], points[5], points[4]],
                                [points[2], points[3], points[7], points[6]],
                                [points[1], points[2], points[6], points[5]],
                                [points[0], points[3], points[7], points[4]]],
                                facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5)
ax[1].add_collection3d(transformasi_sebelum_scale)

# Menambahkan translasi dan skala pada subplot
transformasi_sesudah_translation = Poly3DCollection([[transformed_points_translation[0], transformed_points_translation[1], transformed_points_translation[2], transformed_points_translation[3]],
                                [transformed_points_translation[4], transformed_points_translation[5], transformed_points_translation[6], transformed_points_translation[7]],
                                [transformed_points_translation[0], transformed_points_translation[1], transformed_points_translation[5], transformed_points_translation[4]],
                                [transformed_points_translation[2], transformed_points_translation[3], transformed_points_translation[7], transformed_points_translation[6]],
                                [transformed_points_translation[1], transformed_points_translation[2], transformed_points_translation[6], transformed_points_translation[5]],
                                [transformed_points_translation[0], transformed_points_translation[3], transformed_points_translation[7], transformed_points_translation[4]]],
                                facecolors='magenta', linewidths=1, edgecolors='b', alpha=0.5)
ax[0].add_collection3d(transformasi_sesudah_translation)

transformasi_sesudah_scale = Poly3DCollection([[transformed_points_scale[0], transformed_points_scale[1], transformed_points_scale[2], transformed_points_scale[3]],
                                [transformed_points_scale[4], transformed_points_scale[5], transformed_points_scale[6], transformed_points_scale[7]],
                                [transformed_points_scale[0], transformed_points_scale[1], transformed_points_scale[5], transformed_points_scale[4]],
                                [transformed_points_scale[2], transformed_points_scale[3], transformed_points_scale[7], transformed_points_scale[6]],
                                [transformed_points_scale[1], transformed_points_scale[2], transformed_points_scale[6], transformed_points_scale[5]],
                                [transformed_points_scale[0], transformed_points_scale[3], transformed_points_scale[7], transformed_points_scale[4]]],
                                facecolors='yellow', linewidths=1, edgecolors='g', alpha=0.5)
ax[1].add_collection3d(transformasi_sesudah_scale)

# Menampilkan legenda
ax[0].legend()
ax[1].legend()

# Menyesuaikan batas sumbu
for a in ax:
    a.set_xlim([0, 5])
    a.set_ylim([0, 5])
    a.set_zlim([0, 5])

# Menampilkan plot
plt.show()
