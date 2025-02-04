from collections import Counter

import numpy as np


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D



from performance_metrics import RegressionMetrics

# Generate synthetic dataset with multiple outputs (2 target variables)
X, y = datasets.make_regression(n_samples=100, n_features=3, n_targets=2, noise=20, random_state=42)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add bias term (column of ones) to X for intercept
X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

# Initialize weights (for 3 features + bias term, and 2 output variables)
n_features = X_train.shape[1]
n_outputs = y_train.shape[1]
weights = np.zeros((n_features, n_outputs))

# Hyperparameters
learning_rate = 0.01
n_iters = 1000

# Gradient Descent Algorithm
for i in range(n_iters):
    predictions = X_train @ weights  # Compute predictions
    error = predictions - y_train  # Compute error
    gradients = (1 / X_train.shape[0]) * (X_train.T @ error)  # Compute gradients
    weights -= learning_rate * gradients  # Update weights

    # Compute and print loss every 100 iterations
    if i % 100 == 0:
        loss = RegressionMetrics.mean_squared_error(y_train, predictions)
        print(f"Iteration {i}, Loss: {loss:.4f}")

# Evaluate on test set
y_pred = X_test @ weights
test_loss = RegressionMetrics.mean_squared_error(y_test, y_pred)
print(f"Test Loss: {test_loss:.4f}")

# Visualization of true vs predicted values for first output variable
plt.scatter(y_test[:, 0], y_pred[:, 0], color='blue', label='Output 1')
plt.scatter(y_test[:, 1], y_pred[:, 1], color='red', label='Output 2')
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
plt.title("Multivariate Regression: True vs Predicted")
plt.legend()
plt.show()
