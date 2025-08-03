import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Barplot: Species vs SepalLengthCm
sns.barplot(x='species', y='sepal_length', data=df)
plt.title("Barplot: Species vs Sepal Length")
plt.show()

# Countplot: Count of different species
sns.countplot(x='species', data=df)
plt.title("Countplot: Species Count")
plt.show()

# Boxplot: Species vs SepalWidthCm
sns.boxplot(x='species', y='sepal_width', data=df)
plt.title("Boxplot: Species vs Sepal Width")
plt.show()

# Swarmplot: Species vs SepalWidthCm
sns.swarmplot(x='species', y='sepal_width', data=df)
plt.title("Swarmplot: Species vs Sepal Width")
plt.show()

# Distplot: Distribution of SepalWidthCm
sns.histplot(df['sepal_width'], kde=True)
plt.title("Distribution of Sepal Width")
plt.show()

# Jointplot: SepalWidthCm vs SepalLengthCm
sns.jointplot(x='sepal_width', y='sepal_length', data=df, kind='scatter')
plt.suptitle("Jointplot: Sepal Width vs Sepal Length", y=1.02)
plt.show()

# Pairplot: All features with species as hue
sns.pairplot(df, hue='species')
plt.suptitle("Pairplot of All Features", y=1.02)
plt.show()
