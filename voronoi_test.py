from scipy.spatial import Voronoi, voronoi_plot_2d

import matplotlib.pyplot as plt
import numpy as np

# points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
points = np.array([[0, 0.1, 0.1], [0, 1.2, 0], [0, 2.2, 0], [1.1, 0.3, 1], [1, 1.1, 1], [1.8, 2, 0.9], [2, 0, 1.8], [2, 1, 2], [2, 2, 2]])

vor = Voronoi(points, qhull_options='Qbb Qc Qx') # Use QJ for rectangular inputs
print(vor.ridge_vertices)
print(vor.vertices[vor.ridge_vertices[0]])
# for i in vor.ridge_vertices:
#     print(vor.vertices[i[0]], vor.vertices[i[1]])
print(vor.regions)
print(vor.vertices)
# fig = voronoi_plot_2d(vor)
# plt.show()

#----
# points = np.array([[0, .2], [-.2, 1], [0, 2.1], [1.1, -.1], [1, 1], [0.9, 1.9],[2.2, -0.2], [1.9, 1.1], [2.1, 2.3]])

# from scipy.spatial import Voronoi, voronoi_plot_2d
# vor = Voronoi(points)

# print("points[4] =", points[4])
# print("points =", points)
# print("points1 =", vor.points)
# print("region for point 4 =", vor.point_region[4])
# print("regions =", vor.regions)
# print("ridge_vertices =", vor.ridge_vertices)
# print("vertices for region for point 4 =", vor.regions[vor.point_region[4]])
# print("coordinate of Voronoi vertices associated with point 4:")
# print(vor.vertices[vor.regions[vor.point_region[4]]])