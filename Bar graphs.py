# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

#  Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

#  Set the global palette to 'Blues'
sns.set_palette("Blues")

#  Use Seaborn's countplot() to create a color-coded bar plot representing gender and survival flag.
# Specify the data coordinates, color, order of 'sex' categories, and plot orientation. Also, set a title for your plot.
sns.countplot(data=titanic_df, x="sex", hue="survived", order =["female", "male"], color="cyan").set_title("Gender of Passengers")


plt.show()
