# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This script opens, reads and prints the Iris dataset csv file 
# it will form the basis of the statistical analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
data = pd.read_csv("iris.csv", header=-1) 
#set header =-1 as data in row 0
A = np.array (data)

sum_col = (np.sum(A[:,0]))
avg_col = sum_col/150

print (data)
print (np.min(A[:,0]))
print (np.max(A[:,0]))
print (np.sum(A[:,0]))
print (avg_col)
print ('mean', np.mean(A[:,0]))

print (np.min(A[:,1]))
print (np.max(A[:,1]))
data.groupby(4)[0].min()
#
print("minimum sepal length per species" , data.groupby (4) [0].min())

print("maximum sepal length per species" , data.groupby (4) [0].max())

print("mean sepal length per species" , data.groupby (4) [0].mean())



#plt(data.groupby (4) [0].min())

print (data[4].value_counts())

summary = data.groupby(4)[0].describe()


print (summary)
summary.to_csv('summary.csv')

x, y =[A[:,0],A[:,1]] 
plt.scatter(x, y)
plt.show ()




