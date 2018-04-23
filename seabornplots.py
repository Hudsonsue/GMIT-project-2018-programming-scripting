# Programming and Scripting -iris dataset analysis 
# G00219132 Susan Hudson 
# this explores the use of seaborn to produce plots from the Iris dataset.
# it uses the seaborn statistical data visualization library based on mathplotlib.
# https://seaborn.pydata.org/ and https://seaborn.pydata.org/tutorial.html proved useful sources of information


# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')

# import dataset
df = sns.load_dataset('iris')

print(df)

# use the function regplot to make a scatterplot
sns.regplot(x=df["sepal_length"], y=df["sepal_width"])
plt.legend()
plt.show()

 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()

