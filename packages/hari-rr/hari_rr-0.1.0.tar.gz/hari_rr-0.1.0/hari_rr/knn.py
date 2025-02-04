from imports import datasets , train_test_split , plt , np
from matplotlib.colors import ListedColormap
from random_forest import most_common_label
from performance_metrics import ClassificationMetrics

class KNN:
    def __init__(self , k=3):
        self.k =k

    def fit(self,X,y):
        #  no training , just storing
        self.X_train = X
        self.y_train =y

    def predict(self, X):
        predicted_labels = [ self._helper_method(i) for i in X]
        return np.array(predicted_labels)
    
    def _helper_method(self,X):
        # compute distance
        distance = [ self.euclidean_distance(X, x_train) for x_train in self.X_train ]
        # k - nearest neighbour --> labels 
        k_neigh = np.argsort(distance)[:self.k]
        # majority vote
        k_neigh_label = [ self.y_train[i] for i  in k_neigh]
        return most_common_label(k_neigh_label) 
        

    def euclidean_distance(self,x1,x2):
        return np.sqrt(np.sum(x1-x2)**2)
 
  

if __name__ =="__main__":
    iris = datasets.load_iris()
    X,y =iris.data , iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1234
    )
    cmap = ListedColormap(['#ff0000', '#00ff00', '#0000ff'])
    plt.figure()
    plt.scatter(X[: , 0] , X[:,1], c=y, cmap=cmap , edgecolors='k',s=20)
    plt.show()


    # object creation
    clf = KNN(k=1)
    clf.fit(X_train , y_train)
    y_pred = clf.predict(X_test)

    acc= ClassificationMetrics.accuracy(y_test ,y_pred)

    print(acc)