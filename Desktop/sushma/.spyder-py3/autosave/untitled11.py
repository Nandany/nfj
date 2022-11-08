# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:06:10 2022

@author: SPTINT-13
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-13/Downloads/train.csv")
print(data.head(10))
sns.box(x='Pclass',y='Survived',data=data)
