from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
def perform_cross_validation(X, y, model, cv=5):  # cv is the number of folds
    scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    return scores.mean()

iris = load_iris()
Xall = iris.data
yall = iris.target
Xtrain, Xtest, ytrain, ytest = train_test_split(Xall, yall, test_size=0.2)
X = Xtrain
y = ytrain
model = KNeighborsClassifier()
model.fit(Xtrain, ytrain)

accuracy = perform_cross_validation(Xtest, ytest, model)
print(accuracy)


#scaler = StandardScaler()
#X = scaler.fit_transform(X)

ypred=model.predict(Xtest)

print(confusion_matrix(ypred,ytest))
print(accuracy_score(ypred,ytest))

pickle.dump(model, open(".\Data_Engineer\Flask\Practica_flask\model.pkl", "wb"))