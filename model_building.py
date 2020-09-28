# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:47:22 2020

@author: mosto
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df= pd.read_csv('EDA_data.csv')


df.columns



#Get relevant data
model_data = df[['Avg_salary','Rating','Size',  'Type_of_ownership','Industry', 'Sector', 'Revenue',
                 'Job_State_cleaned','Age', 'Python', 'SQL',
       'AWS', 'AZURE', 'BIG_DATA', 'Computer_Vision', 'R', 'Visualization',
       'Tableau', 'Power BI', 'Machine_Learning', 'STATISTICS',
       'Deep Learning', 'EXCEL', 'Deployment', 'Job_simplified', 'Seniority']]


#Categorical variables to dummy variables


df_dum = pd.get_dummies(model_data)


#train test split

from sklearn.model_selection import train_test_split

X=df_dum.drop('Avg_salary',axis=1)
y=df_dum.Avg_salary.values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
 
 
 
 #Multiple linear regression
 
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()


from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)


np.mean(cross_val_score(lm, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))


#Lasso regression

lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))

alpha =[]
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml=Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring='neg_mean_absolute_error',cv=3)))

plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err,columns=['alpha','error'])
df_err[df_err.error ==max(df_err.error)]
 


#Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring='neg_mean_absolute_error',cv=3)) 



##Tune the model with GridSearch CV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10),'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs=GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train, y_train)


lml.fit(X_train, y_train)


gs.best_score_
gs.best_estimator_



#Test Ensembles

tpred_lm = lm.predict(X_test)
tpred_lml = lml.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)



from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)


mean_absolute_error(y_test,(tpred_lm + tpred_rf)/2)



import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump(pickl,open('model_file'+".p","wb"))


file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']



model.predict(X_test.iloc[1,:].values.reshape(1,-1))
#X_test.iloc[1,:].values



 