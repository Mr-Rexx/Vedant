 import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# os.chdir (r"C:\Users\Vedan\Music\Iris_data.csv")

data = pd.read_csv(r"C:\Users\Vedan\Music\Iris_data.csv", index_col=False)



data.head()

data['Species']=data['Species'].map({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})

req_data=data[data.Species!=2]

# req_data=data[data.Species==1]
req_data.drop(columns='Id', inplace=True)

features=list(set(req_data.columns)-set(['Species']))

x=req_data[features]
xx=req_data[features].values

y=req_data['Species']
yy = req_data['Species'].values


