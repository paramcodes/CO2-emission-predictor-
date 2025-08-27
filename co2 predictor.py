import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
from sklearn import linear_model
data=pd.read_csv("DATA.csv")
X=data[["Weight"]]
y=data[["CO2"]]
regr=linear_model.LinearRegression()
regr.fit(X,y)
arr1=np.array([y])
arr2=np.array([X])
print
PredictedCO2=regr.predict(X)
print(PredictedCO2)

plt.xlabel("Weight")
plt.ylabel("CO2")
plt.scatter(data.Weight,data.CO2,color="blue")
plt.show()
plt.hist(data.Weight,color="green")
plt.show
plt.bar(data.Weight,data.CO2,color="green",width=20)
plt.show()

