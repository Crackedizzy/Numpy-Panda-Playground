# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset.
titanic_df = sns.load_dataset('titanic')

# Create a histogram using Seaborn's histplot() function. Use 'age' as the variable and include KDE. Consider a bin size of 30 for granularity. 
sns.histplot(data = titanic_df, x = "age", kde=True, bins=30, palette="pastel", hue="sex", multiple="stack")

# Set a descriptive and engaging title for your histogram.
plt.title("Age Visualisation using Histograms")

# Clearly label your axes for better readability of the plot. 
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

# Display your histogram using Matplotlib's show() function.
plt.show()