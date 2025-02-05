from collections import Counter

import numpy as np


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D




class LinearRegression:
    def __init__(self , lr = 0.001 , n_iters = 1000):
        self.lr =lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X,y):
        # intializing the empty weights and bias 
        n_samples , n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for i in range(self.n_iters):

            # approximtion
            y_pred = np.dot(X, self.weights) + self.bias
            
            # gradient formula 
            dw = (1/ n_samples) * np.dot(X.T , (y_pred - y ))
            db = (1/ n_samples) * np.sum(y_pred - y )
            
            # updation rule
            self.weights -= self.lr * dw
            self.bias -= self.lr * db


    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred

if __name__ == "__main__":
    features = int(input("Enter the number of features :- "))
    if features==1:
        X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        learning_rates = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 
                          0.00005, 0.00001, 0.000001, 0.0000001]

        # Plot setup
        plt.figure(figsize=(10, 6))
        cmap = plt.get_cmap("viridis")

        for i, lr in enumerate(learning_rates):
            clf = LinearRegression(lr=lr, n_iters=1000)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            # mse_value = RegressionMetrics.mean_squared_error(y_test, y_pred)
            # print(f"Learning rate: {lr}, MSE: {mse_value:.4f}")

            # plt.plot(X_test, y_pred, label=f'LR: {lr}, MSE: {mse_value:.2f}')

        # Scatter actual data points
        plt.scatter(X_train, y_train, color=cmap(0.9), s=10, label="Train Data")
        plt.scatter(X_test, y_test, color=cmap(0.5), s=10, label="Test Data")

        # Final plot adjustments
        plt.xlabel("X values")
        plt.ylabel("Predicted values")
        plt.title("Linear Regression Predictions for Different Learning Rates")
        plt.legend()
        plt.grid()
        plt.show()
    elif features==3:
        X, y = datasets.make_regression(n_samples=100, n_features=3, noise=20, random_state=4)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        
# Train model with a specific learning rate
        model = LinearRegression(lr=0.5, n_iters=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        # mse_value = RegressionMetrics.mean_squared_error(y_test, y_pred)
        # print(f"MSE: {mse_value:.4f}")
        # Create a 3D scatter plot of true vs predicted values
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Plot true values (X_test and y_test)
        ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2], c=y_test, cmap='viridis', s=50, label='True Values')

        # Plot predicted values (X_test and predicted y_pred)
        ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2], c=y_pred, cmap='plasma', marker='^', s=50, label='Predicted Values')

        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_zlabel('Feature 3')
        ax.set_title('3D Scatter Plot of True vs Predicted Values')
        plt.show(block=True)
        
    else:
        X, y = datasets.make_regression(n_samples=100, n_features=features, noise=20, random_state=4)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        learning_rates = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001, 
                          0.00005, 0.00001, 0.000001, 0.0000001]
        for i, lr in enumerate(learning_rates):
            clf = LinearRegression(lr=lr, n_iters=1000)
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)

            # mse_value = RegressionMetrics.mean_squared_error(y_test, y_pred)
            # print(f"Learning rate: {lr}, MSE: {mse_value:.4f}")

        
