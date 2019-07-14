"""


Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota.
 The researchers (Cook and Weisberg, 1999) measured and recorded the following data 
 (Import bluegills.csv File) Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial 
	regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking 
into account a quadratic function of the age of the fish.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("bluegills.csv")
labels=dataset.iloc[:,1].values.reshape(-1,1)
features=dataset.iloc[:,0].values.reshape(-1,1)
"""
plt.scatter(features, labels, color = 'red')
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()
"""
#first handle the missing values
#second process is to handle catagorical data

"""
checkin using linear regression
"""

from sklearn.linear_model import LinearRegression
lin_reg_1=LinearRegression()
lin_reg_1.fit(features,labels)


# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features,lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()


"""
use of the linear regressor method  point is far away from line 
so it is poor testing data and train data both are poor 
this condition is known as underfitting
"""

#now use polynomial regression
# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 4)
features_poly = poly_object.fit_transform(features)
#features_poly  convert x into x^5,x^4,x^3,x^2,x^1,x^0

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)



# Visualising the ploynomial Regression results


plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poly_object.fit_transform(features)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()


















