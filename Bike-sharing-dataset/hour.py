import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hour_dt = pd.read_csv("hour.csv")
hour_dt.head()
hour_dt.info()
hour_dt.isna().sum()
print("Jumlah duplikasi: ", hour_dt.duplicated().sum())

hour_dt['dteday'] = pd.to_datetime(hour_dt['dteday'])
hour_dt['holiday'] = pd.to_datetime(hour_dt['holiday'])
hour_dt['weekday'] = pd.to_datetime(hour_dt['weekday'])
hour_dt['workingday'] = pd.to_datetime(hour_dt['workingday'])
hour_dt.info()
print (hour_dt.info())


hour_dt.describe(include="all")

season_counts = hour_dt.groupby('season')['cnt'].sum().reset_index()
season_counts['season'] = season_counts['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})

print(season_counts)

hour_counts = hour_dt.groupby('hr')['cnt'].sum().reset_index()

print(hour_counts)

plt.figure(figsize=(10, 6))
sns.barplot(data=season_counts, x='season', y='cnt', palette='viridis')
plt.title('Jumlah Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan')
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_counts, x='hr', y='cnt', marker='o')
plt.title('Jumlah Penyewaan Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(range(0, 24))
plt.grid()
plt.show()

user_counts = hour_dt.groupby(['hr'])[['casual', 'registered']].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=user_counts, x='hr', y='casual', label='Pengguna Kasual', marker='o')
sns.lineplot(data=user_counts, x='hr', y='registered', label='Pengguna Terdaftar', marker='o')
plt.title('Jumlah Penyewaan Sepeda per Jam berdasarkan Tipe Pengguna')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(range(0, 24))
plt.legend()
plt.grid()
plt.show()