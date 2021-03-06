#Multiple Linear Regression
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import tensorflow
# data = pd.read_csv("finalrev44.csv")
data = pd.read_csv("outdata2000.csv")
# data = pd.read_csv("CatanDataConvertedTo5InputsAnd1outputCSV.csv")
print(data.head())
data = data[["points", "O", "L", "W", "C", "S"]]
# data = data[["points", "s1tile1", "s1tile2", "s1tile3", "s2tile1", "s2tile2", "s2tile3"]] #-.301269
# data = data[['won', 's1r1', 's1r2', 's1r3', 's2r1', 's2r2', 's2r3']]
# data = data[['points', 's1v1', 's1v2', 's1v3', 's2v1', 's2v2', 's2v3']]
# data = data[['points', 's1v1', 's1r1', 's1v2', 's1r2', 's1v3', 's1r3', 's2v1', 's2r1', 's2v2', 's2r2', 's2v3', 's2r3']]
# data = data[["points", "stot"]]
# predict = #LABEL / WHAT we're looking for
predict = "points"
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=.1)
#test size helps break up data by a factor so that the model has new sets to train / learn on. random_state=0 just added
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc) #Accuracy of the model R2
print("Co: " ,linear.coef_) #The higher the coefficient, the more "weight" that attribute has in the model
print("Intercept: " , linear.intercept_)

predictions = linear.predict(x_test) #takes an array of arrays
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

#GameNum, player number(1-4), ending-victory points, Settlement 1 resource1, Settlement 1 value 1, Settlement 1 resource 2, Settlement 1 value 2, Settlement 1 resource 1, settlement 1

