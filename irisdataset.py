# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This script opens, reads and prints the Iris dataset csv file 
# it will form the basis of the statistical analysis

import numpy as np
import pandas as pd
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

print (np.min(A[:,1]))
print (np.max(A[:,1]))

data.groupby(4)[0].min()
print("minimum sepal length per speices" , data.groupby (4) [0].min())

print("maximum sepal length per speices" , data.groupby (4) [0].max())

print("mean sepal length per speices" , data.groupby (4) [0].mean())


