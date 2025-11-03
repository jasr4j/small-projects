# pip install numpy matplotlib PyQt5

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D  # Import necessary 3D plotting library
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')

# Define the function to minimize
def f(x, y):
    return x**2 + y**2

# Gradient descent algorithm
def gradient_descent(x_start, y_start, learning_rate, num_iterations):
    x_history = [x_start]
    y_history = [y_start]

    for i in range(num_iterations):
        x = x_history[-1]
        y = y_history[-1]

        x_new = x - learning_rate * f(x, y) * 2 * x  # Update with gradient of f
        y_new = y - learning_rate * f(x, y) * 2 * y

        x_history.append(x_new)
        y_history.append(y_new)

    return x_history, y_history

# Set initial values
x_start, y_start = -2, 2
learning_rate = 0.00001
num_iterations = 200000

# Run gradient descent
x_history, y_history = gradient_descent(x_start, y_start, learning_rate, num_iterations)

# Create a grid of points for the 3D plot
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create a 3D plot
fig = plt.figure(figsize=(10, 6))  # Adjust figure size for better visualization
ax = fig.add_subplot(111, projection='3d')

# Plot the contour surface
ax.contourf(X, Y, Z, levels=20, cmap='viridis')  # Use viridis colormap for better visualization

# Plot the gradient descent path in 3D
ax.plot3D(x_history, y_history, [f(x, y) for x, y in zip(x_history, y_history)], 'ro-')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Gradient Descent Visualization (3D)')

plt.show()
