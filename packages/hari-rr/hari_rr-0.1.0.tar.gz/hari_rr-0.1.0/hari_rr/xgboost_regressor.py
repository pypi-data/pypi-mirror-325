
from imports import np  , datasets , train_test_split
from performance_metrics import RegressionMetrics

class ScratchXGBRegressor:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        # Initialize predictions with mean value
        self.init_prediction = np.mean(y)
        y_pred = np.full_like(y, self.init_prediction, dtype=np.float64)

        # Gradient boosting process
        for _ in range(self.n_estimators):
            residual = y - y_pred  # Calculate the residuals (gradient of loss)
            
            # Fit a new tree on the residuals (for simplicity, a regression tree)
            tree = self._build_tree(X, residual)
            self.trees.append(tree)
            
            # Update the prediction
            leaf_values = self._predict_tree(X, tree)
            y_pred += self.learning_rate * leaf_values

    def predict(self, X):
        y_pred = np.full((X.shape[0],), self.init_prediction, dtype=np.float64)
        for tree in self.trees:
            leaf_values = self._predict_tree(X, tree)
            y_pred += self.learning_rate * leaf_values
        return y_pred

    def  _build_tree(self, X, residual):
        # Basic tree building (split features and calculate the residual sum for each split)
        # For simplicity, we are using a decision stump (a tree of depth 1)
        tree = {}
        n_features = X.shape[1]

        best_mse = float('inf')
        best_split = None

        # Try splitting on each feature
        for feature_idx in range(n_features):
            thresholds = np.unique(X[:, feature_idx])

            for threshold in thresholds:
                left_mask = X[:, feature_idx] <= threshold
                right_mask = ~left_mask

                left_residual = residual[left_mask]
                right_residual = residual[right_mask]

                # Check if the left and right subsets are non-empty
                if left_residual.size == 0 or right_residual.size == 0:
                    continue

                # Mean of the residuals for each split (regression tree)
                left_value = np.mean(left_residual)
                right_value = np.mean(right_residual)

                # MSE for this split
                mse = np.mean((left_residual - left_value)**2) + np.mean((right_residual - right_value)**2)

                if mse < best_mse:
                    best_mse = mse
                    best_split = (feature_idx, threshold, left_value, right_value)

        if best_split is None:
            # In case no valid split is found, return a tree that predicts the mean of residuals
            tree['feature_idx'] = -1  # No feature split
            tree['value'] = np.mean(residual)  # Predict the mean of the residuals
        else:
            # Store the best split
            tree['feature_idx'] = best_split[0]
            tree['threshold'] = best_split[1]
            tree['left_value'] = best_split[2]
            tree['right_value'] = best_split[3]
        return tree


    def _predict_tree(self, X, tree):
        # Predict using a single tree
        feature_idx = tree['feature_idx']
        threshold = tree['threshold']
        left_value = tree['left_value']
        right_value = tree['right_value']

        # Leaf assignment based on threshold
        predictions = np.where(X[:, feature_idx] <= threshold, left_value, right_value)
        return predictions


if __name__ == "__main__":
    data = datasets.load_diabetes()
    X = data.data
    y = data.target   
    print(X.shape)
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = ScratchXGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)

    # Train the model
    model.fit(X_train, y_train)

    # Predict with the trained model
    y_pred = model.predict(X_test)

    # Evaluate 
    mse = RegressionMetrics.mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
    rmse = np.sqrt(mse)
    print(f'Root Mean Squared Error: {rmse}')

    tss = np.sum((y_test - np.mean(y_test)) ** 2)

# Calculate the residual sum of squares (RSS)
    rss = np.sum((y_test - y_pred) ** 2)

# Calculate R²
    r2 = 1 - (rss / tss)
    print(f'R2 Error : {r2}')