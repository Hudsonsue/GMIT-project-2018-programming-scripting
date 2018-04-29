# # Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# This programme is a demonstration of basic prediction based on characteristics
# sepal length, petal width and petal length
# based on analysis undertaken by P Hoey 
# http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

print ("basic prediction tool")
print ("---------------------")

sl = float( input("enter sepal length > " ))
sw = float( input("enter sepal width > " ))
pl = float (input("enter petal length > " ))
pw = float(input ("enter petal width > "))
while True:
    if ((sl>6) and (pl >5) and (pw >1.5)):
        print ("most likely Iris virginica!")
    elif ((sl<5.9) and (pl <2) and (pw < 0.7)):
        print ("most likely Iris sertosa!")
    else:
        print ("most likely Iris versicolor!")
    break
