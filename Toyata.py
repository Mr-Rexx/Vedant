import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics

data = pd.read_csv(r"C:\Users\Vedan\OneDrive\Documents\Toyota.csv", index_col=False)

data.describe()

data.head()

req_data=data[['Price', 'KM', 'CC', 'Weight', 'Age', 'HP']]
req_data.describe()
req_data['Age'].unique()
# req_data.fillna(int(req_data['Age'].mean()),inplace=True)


# req_data.replace('??','nan',inplace=True)

symbols = ["??", "????",'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

cars_data1 = pd.read_csv(r"C:\Users\Vedan\OneDrive\Documents\Toyota.csv",index_col=0,
                        na_values=symbols)

req_data=cars_data1[['Price', 'KM', 'CC', 'Weight', 'Age', 'HP']]
req_data = req_data.apply(lambda x:x.fillna(x.mean()) \
                  if x.dtype=='float' else \
                  x.fillna(x.value_counts().index[0])) # or x.mode()[0]

features=list(set(req_data.columns)-set(['Price']))

x=req_data[features]
xx=req_data[features].values

y=req_data['Price']
yy = req_data['Price'].values

train_x,test_x,train_y,test_y=train_test_split(xx,yy, test_size=0.1,random_state=1)

reg = linear_model.LinearRegression()
   
# train the model using the training sets
reg.fit(train_x, train_y)
  
# making predictions on the testing set
y_pred = reg.predict(test_x)
   
# comparing actual response values (y_test) with predicted response values (y_pred)
print("Linear Regression model accuracy(in %):", metrics.r2_score(test_y, y_pred)*100)