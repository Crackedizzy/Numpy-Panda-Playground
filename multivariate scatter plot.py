# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Create a scatter plot depicting the relationship between 'age' and 'fare', 
# distinguishing 'pclass' by hue, 'sex' by markers, and sizes based on the 'fare'.
sns.scatterplot(data=titanic, x="age", y="fare", hue="pclass", style="sex", size="fare", sizes=(20,200))

# Assign a title to the plot
plt.title("Age vs Fare (Separate markers for Sex and Sizes for Fare)")

# Display the plot
plt.show()

# Calculate and print the correlation between all pairs of numerals in the dataset
numerical_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
corr_vars = titanic[numerical_cols].corr()
print(corr_vars)