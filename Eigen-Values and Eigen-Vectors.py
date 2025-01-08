import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64
A=np.array([[4,2],[1,3]])
eigenvalues,eigenvectors=np.linalg.eig(A)
print(eigenvalues,eigenvectors)
print(f"Eigenvalues:{eigenvalues}")
print(f"Eigenvectors:{eigenvectors}")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
origin = np.zeros((2, len(eigenvalues)))
# Origin point for vectors
plt.quiver(*origin, eigenvectors[0, :], eigenvectors[1, :], scale=1, scale_units='xy', angles='xy', color=['r', 'b'])
plt.scatter(eigenvalues, [0, 0], color=['r', 'b'], zorder=3)
plt.title("Eigenvalues and Eigenvectors")
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(-2, 8)
plt.ylim(-1, 15)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

