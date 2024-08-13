# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Set the seaborn default aesthetic parameters
# Choose the "whitegrid" figure style, the "coolwarm" color palette, and scale the font up
sns.set(style = "whitegrid", palette="coolwarm", font = "Serif")

# Create a new figure with a specific size
plt.figure(figsize=(12,6))

# Create a countplot that displays the number of passengers in each class
sns.countplot(x="pclass", data=titanic_df)

# Add a title and labels for the x and y axes
plt.title("Number of Passengers in each class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")

# Rotate the x-axis labels by 30 degrees
plt.xticks(rotation=30)

# Display the plot
plt.show()