# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This script opens, reads and prints the Iris dataset csv file 
# it will form the basis of the statistical analysis
# note - throughout I have used print statements to create empty lines, single, double and multiples

#Import libraries 
# as I built up the script I imported various libraries as needed 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
import datetime
import time


# Below reads in data using Pandas and creates Numpy array of data
# As the csv file I had used throughout had no headers I read in a version and added names to columns for use with pandas' describe.
#

data = pd.read_csv("iris.csv", header=-1) # note I set header =-1 as data in row 0
A = np.array (data) # created a NumpPy array of the dataset
datawithheaders = pd.read_csv("iris.csv", names= ('sepal length', 'sepal width', 'petal length', 'petal width', 'species'))


## Script below allows anyone running script to decide whether to save the print output to file or display in terminal
## if D is selected output will display on terminal
## if S is selected output will be saved to a file
## any other or no selection will result in a display on terminal

while True:
    response = input("Display or save to file? D or S > ")
    if response == "S": 
        sys.stdout=open ('generalstats.txt','w') # redirected to file
        break
    elif response == "D":break    
    elif "D":break


print('\n'*2)
# Below prints the current date and time - acts as timestamp on output file if saved
# http://www.pythonforbeginners.com/basics/python-datetime-time-examples was a useful source I used
 

print ('Output of Irisdataset analysis: Student G00219132, Susan Hudson')
print('\n'*2)
print ('**************************************************')
print ("Run date and time: " ,datetime.datetime.now().strftime("Date: %d-%m-%y    Time: %H-%M"))
print ('**************************************************')
print()
print()

# print (data)  # This printed the dataset and was only used for code checking purposes
# I have used print statements to create empty lines, single, double and multiples

## below are some basic stats for all species

print('BASIC STATISTICS ALL SPECIES')
print('----------------------------')

for i in range (0,4):
    feature = ['sepal length', 'sepal width', 'petal length', 'petal width']
    print ("Minimum", feature [i], "for all species is", np.min(A[:,i]),"cm")
    print ("Maximum", feature [i], "for all species is",np.max(A[:,i]),"cm")
    print ("Mean", feature [i], " for all species is", np.mean(A[:,i]),"cm")
    print()

print('\n')

# below produces basic stats, this time grouped by species
#data.groupby(4)[0].min()

print ('SIMPLE STATISTICS GROUPED BY SPECIES')
print ('------------------------------------')
print()
print("Minimum sepal length per species" , data.groupby (4) [0].min())
print('\n')
print("Maximum sepal length per species" , data.groupby (4) [0].max())
print('\n')
print("Mean sepal length per species" , data.groupby (4) [0].mean())


print('\n')
print("Minimum sepal width per species" , data.groupby (4) [1].min())
print('\n')
print("Maximum sepal width per species" , data.groupby (4) [1].max())
print('\n')
print("Mean sepal width per species" , data.groupby (4) [1].mean())


print('\n')
print("Minimum petal length per species" , data.groupby (4) [2].min())
print('\n')
print("Maximum petal length per species" , data.groupby (4) [2].max())
print('\n')
print("Mean petal length per species" , data.groupby (4) [2].mean())


print('\n')
print("Minimum petal width per species" , data.groupby (4) [3].min())
print('\n')
print("Maximum petal width per species" , data.groupby (4) [3].max())
print('\n')
print("Mean petal width per species" , data.groupby (4) [3].mean())


##below prints number of records per species
print('\n') 
print ("Number of records per species")
print ('-----------------------------')
print (data[4].value_counts())

print('\n')

# Below uses the describe function to produce some statistics of the Iris dataset
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html
# Additional sources of reference, when troubleshooting are listed below
# 
# https://stackoverflow.com/questions/32835498/pantdas-python-describe-formatting-output 
# https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe 
# 
# Iinitially created separate scripts for each feature but then wrote a looped version of the script
# I used GMIT Programming & Scripting course videos to assist in looped script

 
print ('STATISTICS USING DESCRIBE')
print ('-------------------------') 

# Script below produces statistics for features across all species 
# it is displayed and also saved to csv file summary.csv

print ('statistics for each feature for all species')
print ('-------------------------------------------')
print()
features_all = datawithheaders.describe ()
print (features_all)
features_all.to_csv('summary.csv')
print('\n')



# Below is a loop to print statistcs using describe grouped by species

for i in range (0,4):
    summary = data.groupby(4)[i].describe()
    feature = ['sepal length', 'sepal width', 'petal length', 'petal width']
    print ("Summary of data set",feature[i])
    print ('---------------------------------')
    print()
    print (summary)
    print()
print('\n')
print('\n')

# Below uses  matplotlib.pyplot to produce and save scatter graphs
# plt.ioff()

# Sepal characteristics
x, y =[A[:,0],A[:,1]] 
plt.xlabel('Sepal Length', fontsize = 14)
plt.ylabel("Sepal Width", fontsize = 14)
plt.title("Iris Datset: Sepal Charateristics", fontsize = 18)
plt.scatter(x, y)
plt.savefig ('Sepal.png') #saves plot as sepal.png image
plt.show () #displays plot om termial
## note: must save before show as otherwise blank file!

# Petal charateristics
# below is similar to sepal plot with an attempt to distinguish different species by colour
# it did now work but I am leaving my attempt as may revisit when knowledge grows

for i in range (0,len(A)-1):

        x, y =[A[i][2],A[i][3]] 
        flower = A[i][4]
        colors =['red', 'blue', 'green']
        if flower=='Iris-setosa':
            color ='green'
        #elif flower =='Iris-versicolor':
         #   color="blue" 
        #elif flower =='Iris-virginica':
         #   color = "green"
        #print (flower) ##check loop OK
         #   print(x,y)     ##check loop OK
        #colors =['red', 'green', 'blue']
        plt.scatter(x, y, c=colors)

#plt.colors(A[i:,4]=="Iris-versicolor",color="blue")
#plt.colors(A[i:,4]=="Iris-virginica",color="red")
plt.xlabel('Petal Length', fontsize = 14)
plt.ylabel("Petal Width", fontsize = 14)
plt.title("Iris Datset: Petal Charateristics", fontsize = 18)
plt.legend
plt.scatter(x, y)
plt.savefig ('Petal.png')
plt.show ()


PetalWidth1 = 0
PetalWidth2 = 0
Irisvirginicacount = 0
multicond = 0


i=0
for i in range (-1,149):
    if A[i][3] == 1:
        PetalWidth1 = PetalWidth1 + 1
    if  A[i][3] == 2:
        PetalWidth2 = PetalWidth2 + 1

    if  ((A[i][3] > 1.5) and (A[i][3] < 2.5) and (A[i][4] == 'Iris-virginica')):
        Irisvirginicacount = Irisvirginicacount +1

    if ((A[i][0] < 6) and (A[i][2]>=4)and (A[i][4] == 'Iris-versicolor')) or ((A[i][3] > 1.5) and (A[i][3] < 2.0) and (A[i][4] == 'Iris-virginica')):
       multicond = multicond +1
       continue

print ("Number of flowers with Petal Width 1cm", PetalWidth1)
print ("Number of flowers with Petal Width 2cm", PetalWidth2)
print ("Number of Iris-virginica >1.5 and <2.5 cm", Irisvirginicacount)
print ("multi cond", multicond)