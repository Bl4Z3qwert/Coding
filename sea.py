import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data= pd.read_csv('.venv/USA_housing.csv')
  
#print(data.shape)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Avg. Area Income', y='Avg. Area House Age', data=data, hue='Avg. Area Number of Rooms')
plt.title('Average Area Income vs Average Area House Age')
plt.xlabel('Average Area Income')
plt.ylabel('House ARea income')
plt.tight_layout()
plt.show()