# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset.
titanic_df = sns.load_dataset('titanic')

# TODO: Create a histogram using Seaborn's histplot() function. Use 'age' as the variable and include KDE. Consider a bin size of 30 for granularity. 
sns.histplot(data = titanic_df, x = "age", kde=True, bins=30, palette="pastel", hue="sex", multiple="stack")

# TODO: Set a descriptive and engaging title for your histogram.
plt.title("Age Visualisation using Histograms")

# TODO: Clearly label your axes for better readability of the plot. 
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

# TODO: Display your histogram using Matplotlib's show() function.
plt.show()