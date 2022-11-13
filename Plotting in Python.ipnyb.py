# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 09:07:08 2022

@author: Vedan
"""

import numpy as np

x=np.arange(0,20,0.1)

y=np.sin(x)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.title('Sinwave 1')
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(x[0:158],y[0:158],marker='.', color ='red', linewidth=7.0)

class A4():
    def __init__(self,height=10,Age=15,Weight=35):
        self.height=height
        self.Age=Age
        self.Weight=Weight
    human=True
    Jolly =3
    
import math
class Circle():
    is_shape = True
    
    def ___init__(self,radius,color='red'):
        self.radius = radius
        self.color = color
        
    def area(self):
        return math.pi * self.radius ** 2
    
    
    
import numpy as np
import matplotlib.pyplot as plt
data = np.array([
    [2,3,4,5],
    [3,4,5,1],
    [2,1,4,6],
    [1,4,6,8],
])

import seaborn as sns

sns.heatmap(data, annot=True)#, ['Health', 'Teachers', 'Time', 'Marks'], ['A', 'B', 'C', 'D'],
# cmap='YlGn', cbarlabel='Number of Students')
# texts = annotate_heatmap(im, valfmt="{x}") 

   
    
    
    