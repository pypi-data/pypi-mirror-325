import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ScratchXGBClassifier:
    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        # Initialize predictions with log-odds (logistic regression)
        self.init_prediction = np.mean(y)
        y_pred = np.full_like(y, self.init_prediction, dtype=np.float64)

        # Gradient boosting process
        for _ in range(self.n_estimators):
            residual = self._compute_residuals(y, y_pred)  # Calculate the residuals (gradient of loss)
            
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
        return self._sigmoid(y_pred) > 0.5  # Convert to binary predictions (0 or 1)

    def _compute_residuals(self, y, y_pred):
        # Compute the residuals (gradient of log loss for binary classification)
        return y - self._sigmoid(y_pred)

    def _sigmoid(self, x):
        # Sigmoid function
        return 1 / (1 + np.exp(-x))

    def _build_tree(self, X, residual):
        # Basic tree building (split features and calculate the residual sum for each split)
        # For simplicity, we are using a decision stump (a tree of depth 1)
        tree = {}
        n_features = X.shape[1]

        best_loss = float('inf')
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

                # Compute log loss (binary cross-entropy) for this split
                left_loss = self._log_loss(left_residual, left_value)
                right_loss = self._log_loss(right_residual, right_value)

                # Total loss for this split
                total_loss = left_loss + right_loss

                if total_loss < best_loss:
                    best_loss = total_loss
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

    def _log_loss(self, y_true, y_pred):
        # Binary log loss (cross-entropy loss)
        epsilon = 1e-15  # To avoid log(0)
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    def _predict_tree(self, X, tree):
        # Predict using a single tree
        feature_idx = tree['feature_idx']
        threshold = tree['threshold']
        left_value = tree['left_value']
        right_value = tree['right_value']

        # Leaf assignment based on threshold
        predictions = np.where(X[:, feature_idx] <= threshold, left_value, right_value)
        return predictions

# Load a classification dataset (Breast Cancer dataset)
data = load_breast_cancer()
X = data.data
y = data.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = ScratchXGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)

# Train the model
model.fit(X_train, y_train)

# Predict with the trained model
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
