
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-whitegrid')
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

# use the function regplot to make a scatterplot
sns.regplot(x=df["sepal_length"], y=df["sepal_width"])
plt.show()

 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()

 