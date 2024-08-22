# Importing required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset 
titanic_df = sns.load_dataset('titanic')

# Create a boxplot to illustrate the relationship between the fare and passenger class, categorized by their survival status.
sns.boxplot(data=titanic_df, x="pclass", y="fare", hue="survived", hue_order=[1,0], palette="Set3", order=[3,1,2])

# Set a fitting title for the plot
plt.title("Box Plot: Passenger Class vs Fare. Highlighting Survival Status")

# Finally, display the plot
plt.show()