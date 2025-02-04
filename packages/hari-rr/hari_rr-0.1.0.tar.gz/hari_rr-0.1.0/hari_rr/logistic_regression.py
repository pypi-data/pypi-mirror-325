# Approximation :- f(w)
# cross entropy , no mse
# gradient descent


from imports import np , datasets , train_test_split

from performance_metrics import ClassificationMetrics

class LogisticRegression:
    def __init__(self , lr = 0.001 , n_iters = 1000):
        self.lr =lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self , X,y):
        # initialize the parameters        
        n_samples , n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0      

        # gradient descent
        for i in range(self.n_iters): 
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear_model)

            # updating weights
            dw = (1/ n_samples) * np.dot(X.T , (y_pred - y ))
            db = (1/ n_samples) * np.sum(y_pred - y )

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = self.sigmoid(linear_model)

        return [1 if i>=0.5 else 0 for i in y_pred ]
    
    def sigmoid(self, X):
        return 1/ (1+np.exp(-X))
    

if __name__ =="__main__":
    data = datasets.load_breast_cancer()
    X = data.data  # Feature matrix
    y = data.target  # Target labels

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )

    # Initialize the RandomForest classifier with 3 trees and max depth of 10
    clf =  LogisticRegression(lr=0.0001 , n_iters=1000)

    # Train the classifier on the training set
    clf.fit(X_train, y_train)

    # Predict the labels for the test set
    y_pred = clf.predict(X_test)

    # Calculate the accuracy of the model
    acc = ClassificationMetrics. accuracy(y_test, y_pred)

    # Print the accuracy
    print("Accuracy:", acc)
