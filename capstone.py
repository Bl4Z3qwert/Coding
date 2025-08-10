import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("IMDB Dataset.csv")

print(df.head(3))
print(df.tail(3))
df.info()
print(df.isnull().sum())

subset_df = df.iloc[40:75]
print(subset_df)

max_votes = df[df['Votes'] == df['Votes'].max()]
print(max_votes)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x=df['IMDB_Rating'])
plt.title("Boxplot of IMDB Rating")

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Runtime'])
plt.title("Boxplot of Runtime")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.6)
plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")
plt.title("IMDB Rating vs Runtime")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df['IMDB_Rating'], kde=True)
plt.title("Distribution of IMDB Rating")

plt.subplot(1, 2, 2)
sns.histplot(df['Runtime'], kde=True)
plt.title("Distribution of Runtime")
plt.tight_layout()
plt.show()

plt.figure((figsize)=(10, 6))