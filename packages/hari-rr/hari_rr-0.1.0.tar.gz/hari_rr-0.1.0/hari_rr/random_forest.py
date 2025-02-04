from imports import np , Counter , datasets , train_test_split
import hari_rr.decision_tree_classifier as decision_tree_classifier
from performance_metrics import ClassificationMetrics


# Function to create a bootstrap sample from the dataset
def bootstrap_sample(X, y):
    n_samples = X.shape[0]  # Get the number of samples in the dataset
    idxs = np.random.choice(n_samples, n_samples, replace=True)  # Randomly sample with replacement
    return X[idxs], y[idxs]

# Function to find the most common label in an array
def most_common_label(y):
    counter = Counter(y)  # Count occurrences of each label
    most_common = counter.most_common(1)[0][0]  # Get the most frequent label
    return most_common

# Random Forest Classifier implementation
class RandomForest:
    def __init__(self, n_trees=10, min_samples_split=2, max_depth=100, n_feats=None):
        self.n_trees = n_trees  # Number of decision trees in the forest
        self.min_samples_split = min_samples_split  # Minimum samples required to split a node
        self.max_depth = max_depth  # Maximum depth of each tree
        self.n_feats = n_feats  # Number of features to consider for each split
        self.trees = []  # List to store the decision trees

    # Fit the RandomForest model to the data
    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = decision_tree_classifier.DecisionTree(
                min_samples_split=self.min_samples_split,
                max_depth=self.max_depth,
                n_feats=self.n_feats,
            )
            X_samp, y_samp = bootstrap_sample(X, y)  # Create bootstrap sample
            tree.fit(X_samp, y_samp)  # Train decision tree on bootstrap sample
            self.trees.append(tree)  # Store trained tree

    # Predict labels for input data
    def predict(self, X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])  # Collect predictions from all trees
        # [[1111] [1010] [1011] ]
        # after swapping > [[111] [100] [111] [101] ]
        tree_preds = np.swapaxes(tree_preds, 0, 1)  # Transpose to align predictions per sample
        y_pred = [most_common_label(tree_pred) for tree_pred in tree_preds]  # Take majority vote
        # majority voting -> [ 1 , 0 , 1, 1 ]
        return np.array(y_pred)  # Return final predictions

# Testing the RandomForest implementation
if __name__ == "__main__":
    # Load the breast cancer dataset
    data = datasets.load_breast_cancer()
    X = data.data  # Feature matrix
    y = data.target  # Target labels

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    # Initialize the RandomForest classifier with 3 trees and max depth of 10
    clf = RandomForest(n_trees=3, max_depth=10)

    # Train the classifier on the training set
    clf.fit(X_train, y_train)

    # Predict the labels for the test set
    y_pred = clf.predict(X_test)

    # Calculate the accuracy of the model
    acc = ClassificationMetrics.accuracy(y_test, y_pred)

    # Print the accuracy
    print("Accuracy:", acc)
