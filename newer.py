import pandas as pd

import matplotlib.pyplot as plt

# URL for the Google Sheets CSV export

url = "https://docs.google.com/spreadsheets/d/19DuqMX-N6nDUnLMsYn_1EojQJhIfdZT98NJfWZTR9nA/export?format=csv&id=19DuqMX-N6nDUnLMsYn_1EojQJhIfdZT98NJfWZTR9nA&gid=1362010949"

weather = pd.read_csv(url)
print(weather.head())
weather['date_time'] = pd.to_datetime(weather['date_time'], format='%d-%m-%Y %H:%M')
plt.figure(figsize=(10, 5))
plt.plot(weather['date_time'], weather['temperature'], label='Temperature', color='tab:blue')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()





plt.figure(figsize=(8, 6))
plt.scatter(weather['date_time'], weather['humidity'], c='tab:blue', label='Humidity', alpha=0.5)
plt.xlabel('Date and Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(weather['temperature'], weather['humidity'], c='tab:green', alpha=0.5)
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Temperature vs Humidity')
plt.tight_layout()
plt.show()