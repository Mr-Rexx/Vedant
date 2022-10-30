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
