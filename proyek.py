import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def transformasi_affine(titik, matrix, translation):
    transformed_titik = np.dot(titik, matrix.T) + translation
    return transformed_titik

def matrix_skala(scaling_factors):
    return np.diag(scaling_factors)

# Titik-titik kubus
titik = np.array([
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
translation_vector = np.array([2, 2, 0])#menentukan translasi

# Melakukan translasi affine
titik_translasi = transformasi_affine(titik, affine_matrix_translation, translation_vector)

# Matriks skala affine
scaling_factors = np.array([2, 1, 1])#menentukan skala
affine_matrix_scale = matrix_skala(scaling_factors)

# Melakukan transformasi skala
titik_skala = transformasi_affine(titik, affine_matrix_scale, np.zeros(3))

# Membuat plot 3D
fig, ax = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})

# Plot untuk translasi sebelum
ax[0].set_title('Objek Sebelum Translasi')
transformasi_sebelum_translation = Poly3DCollection([[titik[0], titik[1], titik[2], titik[3]],
                                [titik[4], titik[5], titik[6], titik[7]],
                                [titik[0], titik[1], titik[5], titik[4]],
                                [titik[2], titik[3], titik[7], titik[6]],
                                [titik[1], titik[2], titik[6], titik[5]],
                                [titik[0], titik[3], titik[7], titik[4]]],
                                facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5, label='Sebelum Translasi')
ax[0].add_collection3d(transformasi_sebelum_translation)

# Plot untuk skala sebelum
ax[1].set_title('Objek Sebelum Skala')
transformasi_sebelum_scale = Poly3DCollection([[titik[0], titik[1], titik[2], titik[3]],
                                [titik[4], titik[5], titik[6], titik[7]],
                                [titik[0], titik[1], titik[5], titik[4]],
                                [titik[2], titik[3], titik[7], titik[6]],
                                [titik[1], titik[2], titik[6], titik[5]],
                                [titik[0], titik[3], titik[7], titik[4]]],
                                facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.5, label='Sebelum Skala')
ax[1].add_collection3d(transformasi_sebelum_scale)

# Plot untuk translasi setelah
transformasi_sesudah_translasi = Poly3DCollection([[titik_translasi[0], titik_translasi[1], titik_translasi[2], titik_translasi[3]],
                                [titik_translasi[4], titik_translasi[5], titik_translasi[6], titik_translasi[7]],
                                [titik_translasi[0], titik_translasi[1], titik_translasi[5], titik_translasi[4]],
                                [titik_translasi[2], titik_translasi[3], titik_translasi[7], titik_translasi[6]],
                                [titik_translasi[1], titik_translasi[2], titik_translasi[6], titik_translasi[5]],
                                [titik_translasi[0], titik_translasi[3], titik_translasi[7], titik_translasi[4]]],
                                facecolors='magenta', linewidths=1, edgecolors='b', alpha=0.5, label='Setelah Translasi')
ax[0].add_collection3d(transformasi_sesudah_translasi)
ax[0].set_title('Transformasi Translasi')  # Tambahkan judul

# Plot untuk skala setelah
transformasi_sesudah_skala = Poly3DCollection([[titik_skala[0], titik_skala[1], titik_skala[2], titik_skala[3]],
                                [titik_skala[4], titik_skala[5], titik_skala[6], titik_skala[7]],
                                [titik_skala[0], titik_skala[1], titik_skala[5], titik_skala[4]],
                                [titik_skala[2], titik_skala[3], titik_skala[7], titik_skala[6]],
                                [titik_skala[1], titik_skala[2], titik_skala[6], titik_skala[5]],
                                [titik_skala[0], titik_skala[3], titik_skala[7], titik_skala[4]]],
                                facecolors='yellow', linewidths=1, edgecolors='g', alpha=0.5, label='Setelah Skala')
ax[1].add_collection3d(transformasi_sesudah_skala)
ax[1].set_title('Transformasi Skala')  # Tambahkan judul

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
