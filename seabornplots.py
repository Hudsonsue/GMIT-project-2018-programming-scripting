# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# this explores the use of seaborn to produce plots from the Iris dataset.
# it uses the seaborn statistical data visualization library based on mathplotlib.
# https://seaborn.pydata.org/ and https://seaborn.pydata.org/tutorial.html proved useful sources of information


# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset from seaborn
df = sns.load_dataset('iris')

# below is a piece of code that will prompt the user to select whether they wish to see the dataset displayed.
# if Y is chosen it wil display, otherwise it won't.
while True:
    show = input ("do you want to display the dataset?, enter Y for Yes, N for No > ")
    if show == "Y":
        print(df) #printing the data
        break
    elif show == "N":
        break
    elif "N":
        break

# below runs a seaborn scatter plot of sepal length & width
# It uses 'hue' to change colours by species
# it places a legend in the bottom right of the plot
# user is asked whether they want regression lines or not, if invalid selection made will assume no regression lines
while True:
    response = input ("do you want to show regression in this scatter plot, Y or N > ")
    if response =="Y":
        sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg= True, hue='species')
        break
    elif response =="N":
        sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg= False, hue='species')
        break
    elif "N":
        sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg= False, hue='species')
        break
plt.legend(loc='lower right')
plt.xlabel('Sepal Length', fontsize = 10)
plt.ylabel("Sepal Width", fontsize = 10)
plt.title("Iris Datset: Sepal Charateristics")
plt.tight_layout
plt.show()


# below plots petal length and width in a scatter plot
# It uses 'hue' to change colours by species
# it places a legend in the bottom right of the plot
# it does not have regression lines
sns.lmplot( x="petal_length", y="petal_width", data=df, fit_reg=False, hue='species', legend=False)
plt.title("Iris Datset: Petal Charateristics")
plt.xlabel('Petal Length', fontsize = 10)
plt.ylabel("Petal Width", fontsize = 10)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()


# Histograms of features
# Initial individual plots of two of the features, petal length and sepal length
# Histogram of petal length
# Set default Seaborn style

sns.set()
# Plot histogram of petal lengths
plt.hist(df["petal_length"], bins=20 )
plt.title("Iris Datset: Petal length")
plt.xlabel('Petal Length Bands', fontsize = 10)
plt.ylabel("Instances", fontsize = 10)
plt.show() # Show histogram

# Histogram of sepal length
# Set default Seaborn style
#sns.set()
# Plot histogram of sepal lengths
plt.hist(df["sepal_length"], bins=20 )
plt.title("Iris Datset: sepal length")
plt.xlabel('Sepal Length Bands', fontsize = 10)
plt.ylabel("Instances", fontsize = 10)
plt.show()# Show histogram

# below is a seaborn plot with histograms of all chaaacteristics
# included to show how powerful libraries are !
# histograms
df.hist()
plt.show()









