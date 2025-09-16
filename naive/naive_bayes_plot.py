import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from matplotlib.colors import ListedColormap

# 1. Generate a toy dataset (2 features for easy plotting)
X, y = make_classification(
    n_features=2,      # two features (for 2D plotting)
    n_redundant=0, 
    n_informative=2, 
    n_clusters_per_class=1, 
    n_samples=200,
    random_state=42
)

# 2. Train a Naive Bayes classifier
model = GaussianNB()
model.fit(X, y)

# 3. Plot decision boundaries
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Custom colors for classes
cmap_background = ListedColormap(['#FFAAAA', '#AAAAFF'])
cmap_points = ListedColormap(['#FF0000', '#0000FF'])

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_background)  # decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_points, edgecolor='k', s=40)  # points

plt.title("Naive Bayes Classification with Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
