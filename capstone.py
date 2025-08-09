import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
df= pd.read_csv(url)
print(df.head())
print(df.describe())
print('n\Missing values:', df.isnull().sum())
corr=df.select_dtypes(include=np.number).corr()
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


df.hist(figsize=(10,6), bins=20)
plt.tight_layout()
plt.show()


sns.boxplot(x='species', y='bill_length_mm', data=df)
plt.title('Bill Length by Species')
plt.show()