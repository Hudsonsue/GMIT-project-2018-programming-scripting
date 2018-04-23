
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
print(df)
# use the function regplot to make a scatterplot
sns.regplot(x=df["sepal_length"], y=df["sepal_width"])
plt.show()

 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()

 # Petal charateristics

for i in range (0,len(df)-1):
    x, y =[df[i][2],df[i][3]] 
    ##flower = flower_type[i].decode("utf-8")
	##color = ""

    flower = df[i][4]
    
	#flower = flower_type[i].decode("utf-8")
    #color = ""
    if flower=='Iris-setosa':color ="red"
    elif flower =='Iris-versicolor':color="blue"
    elif flower =='Iris-virginica':color = "green"
      #  print (flower)
       # print(x,y)
   
    sns.scatter(x, y)

#plt.colors(A[:,4]=="Iris-versicolor",color="blue")
#plt.colors(A[:,4]=="Iris-virginica",color="red")
plt.xlabel('Petal Length', fontsize = 14)
plt.ylabel("Petal Width", fontsize = 14)
plt.title("Iris Datset: Petal Charateristics", fontsize = 18)
plt.scatter(x, y)
plt.savefig ('Petal.png')
plt.show ()


