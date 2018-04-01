
"""
Created on Wed Mar 28 13:25:19 2018

@author: paragasa
"""
#Nonlinear Regressor- Polynomial


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
#dataset has position based on level
X = dataset.iloc[:, 1:2].values #upper bound exclusion
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
'''from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
'''

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


#Fit Polynomial Regression to dataset
from sklearn.preprocessing import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
#need to create polynomial X and fit it into a lniear regressor
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


#Visualization of Polynomial Regression results
X_grid = np.arange(min(X), max(X), 0.1) #grid to make curve
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Poly Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


#predicting result with Poly regression

lin_reg_2.predict(poly_reg.fit_transform(6.5))


