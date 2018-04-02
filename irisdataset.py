# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This script opens, reads and prints the Iris dataset csv file 
# it will form the basis of the statistical analysis

import numpy as np
import pandas as pd
import csv
data = pd.read_csv("iris.csv", header=-1)
A = np.array (data)
print (data)
