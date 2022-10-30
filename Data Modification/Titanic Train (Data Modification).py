# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os

os.chdir(r"C:\Users\Vedan\Downloads")

data = pd.read_csv(r"titanic_train.csv")

import numpy as np

data['required']=np.where((data['Survived']==1) & (data['Sex']=='male'),1,0)

req_data=data[data.required==1]

data['neccesary']=np.where((data['Survived']==1) & (data['Sex']=='female'),1,0)

req_dara=data[data.required==1]

data['imperative']=np.where((data['Survived']==1) & (data['Sex']=='female') & (data['Age']>=30),1,0)

req_data=data[data.required==1]

data['imperative']=np.where((data['Survived']==0) & (data['Sex']=='female') & (data['Age']>=30),1,0)

req_data=data[data.required==1]

x=np.arange(0,10,0.1)

y=np.sin(x)


