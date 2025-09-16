import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# Example dataset
X = np.array([[1,2],[2,1],[3,3],[6,5],[7,8],[8,6]])
y = np.array([0,0,0,1,1,1])   # labels

# Train Naive Bayes
# GaussianNB Naive Bayes classifier
model = GaussianNB().fit(X, y)

# Create a mesh grid for the decision boundary
x_min = X[:,0].min()-1
x_max = X[:,0].max()+1

y_min = X[:,1].min()-1
y_max = X[:,1].max()+1

xx, yy = np.meshgrid(
            np.linspace(x_min, x_max, 200),
            np.linspace(y_min, y_max, 200)
        )

# Predict class for each point in the grid
Z = model.predict(
        np.c_[xx.ravel(), yy.ravel()]
    )

Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)

# Plot training points
plt.scatter(X[:,0], X[:,1], c=y, edgecolor='k')

plt.title("Naive Bayes with Decision Boundary")
plt.show()
