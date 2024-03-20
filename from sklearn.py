from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load iris dataset as an example
iris = load_iris()
X = iris.data
Y = iris.target

# split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# train a random forecast classifier
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X_train, Y_train)

# predict on test data
Y_pred = clf.predict(X_test)

# calculate accuracy
print(f'Accuracy: {accuracy_score(Y_test, Y_pred)}')