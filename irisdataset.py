# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This script opens, reads and prints the Iris dataset csv file 
# it will form the basis of the statistical analysis
# note - throughout I have used print statements to create empty lines, single, double and multiples

#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys

## below allows anyone running script to decide whether to save the print output to file or display in terminal

# select plot style
plt.style.use('seaborn-whitegrid')

# below reads in data using Pandas and creates Numpy array of data
data = pd.read_csv("iris.csv", header=-1) # note I set header =-1 as data in row 0
A = np.array (data) # created a NumpPy array of the dataset

## Script below allows anyone running script to decide whether to save the print output to file or display in terminal
## if D is selected output will display on terminal
## if S is selected output will be saved to a file
## any other or no selection will result in a display on terminal

while True:
    response = input("Display or save to file? D or S > ")
    if response == "S": 
        sys.stdout=open ('generalstats.txt','w') # redirected to file
        break###turns off interactieve display
    elif response == "D":break    
    elif "D":break

    
sum_col = (np.sum(A[:,0]))
avg_col = sum_col/150

print (data)  # This printed the dataset 

## used print statements to create empty lines, single, double and multiples

print('\n'*2)


## below are some basic stats for all species
print ('SIMPLE STATISTICS FOR ALL MEASUREMENTS')
print ("Minimum Sepal length all species is",np.min(A[:,0]),"cm")
print ("Maximum Sepal length all species is",np.max(A[:,0]),"cm")
print ("Mean Sepal length all species is", np.mean(A[:,0]),"cm")
print()
print ("Minimum Sepal width all species is",np.min(A[:,1]),"cm")
print ("Maximum Sepal width all species is",np.max(A[:,1]),"cm")
print ('Mean Sepal width all species is', np.mean(A[:,1]),"cm")
print()
print ("Minimum Petal Length all species is",np.min(A[:,2]),"cm")
print ("Maximum Petal Length all species is",np.max(A[:,2]),"cm")
print ('Mean Petal Length all species is', np.mean(A[:,2]),"cm")
print()
print ("Minimum Petal width all species is",np.min(A[:,3]),"cm")
print ("Maximum Petal width all species is",np.max(A[:,3]),"cm")
print ('Mean Petal width all species is', np.mean(A[:,3]),"cm")

# below produces basic stats, this time grouped by species
#data.groupby(4)[0].min()

print ('SIMPLE STATISTICS GROUPED BY SPECIES')

print('\n')
print("Minimum sepal length per species" , data.groupby (4) [0].min())
print('\n')
print("Maximum sepal length per species" , data.groupby (4) [0].max())
print('\n')
print("Mean sepal length per species" , data.groupby (4) [0].mean())


##below prints number of records per species
print('\n') 
print ("Number of records per species")
print (data[4].value_counts())

print('\n')

# below uses the describe function to produce some statistics of the Iris dataset
# it is displayed and also saved to csv file summary.csv

print('\n')

# below uses the describe function to produce some general statistics of the Iris dataset
# it is displayed and also saved to csv file summary.csv

print ('STATISTICS USING DESCRIBE FUCTION - output displayed and saved to summary.csv')
summary = data.groupby(4)[0].describe()
print (" Summary of data set", summary)
summary.to_csv('summary.csv')


# Below uses  matplotlib.pyplot to produce and save scatter graphs

  
## plt.ioff()

# Sepal characteristics
x, y =[A[:,0],A[:,1]] 
plt.xlabel('Sepal Length', fontsize = 14)
plt.ylabel("Sepal Width", fontsize = 14)
plt.title("Iris Datset: Sepal Charateristics", fontsize = 18)
plt.scatter(x, y)
plt.savefig ('Sepal.png')

plt.show ()
## note: must save before show as otherwise blank file!

# Petal charateristics

for i in range (0,len(A)-1):
    x, y =[A[i][2],A[i][3]] 
    ##flower = flower_type[i].decode("utf-8")
	##color = ""

    flower = A[i][4]
    
	#flower = flower_type[i].decode("utf-8")
    #color = ""
    if flower=='Iris-setosa':color ="red"
    elif flower =='Iris-versicolor':color="blue"
    elif flower =='Iris-virginica':color = "green"
      #  print (flower)
       # print(x,y)
   
    plt.scatter(x, y)

#plt.colors(A[:,4]=="Iris-versicolor",color="blue")
#plt.colors(A[:,4]=="Iris-virginica",color="red")
plt.xlabel('Petal Length', fontsize = 14)
plt.ylabel("Petal Width", fontsize = 14)
plt.title("Iris Datset: Petal Charateristics", fontsize = 18)
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

    #if (((A[i][0] < 6) and (A[i][2]>=4)and (A[i][4] == 'Iris-versicolor')
     #   or if ((A[i][3] > 1.5) and (A[i][3] < 2.0) and (A[i][4] == 'Iris-virginica'))):
      #  multicond = multicond +1
       # continue

print ("Number of flowers with Petal Width 1cm", PetalWidth1)
print ("Number of flowers with Petal Width 2cm", PetalWidth2)
print ("Number of Iris-virginica >1.5 and <2.5 cm", Irisvirginicacount)
#print ("multi cond", multicond)