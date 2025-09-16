import numpy as np
import matplotlib.pyplot as plt
# quickly generate a fake dataset
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB

# 1. Generate toy dataset
X, y = make_classification(
    n_features=2, #Total number of features
    n_informative=2, #useful features
    n_redundant=0, #useless features
    n_clusters_per_class=1, #How many sub-clusters inside each class.
    n_samples=200, #data points (rows)
    random_state=42 #for randomness
)

# 2. Train Naive Bayes
# Naive Bayes classifier
model = GaussianNB().fit(X, y)

# 3. Decision boundary grid
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 200),
                     np.linspace(X[:,1].min()-1, X[:,1].max()+1, 200))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# 4. Plot
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k')
plt.title("Naive Bayes Classification")
plt.show()
