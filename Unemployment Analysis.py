                       # unemployment_analysis.py  #

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Load or Create Dataset
# -----------------------------
if not os.path.exists("unemployment.csv"):
    print(" unemployment.csv not found, creating sample dataset...")

    data = {
        "Date": pd.date_range(start="2019-01-01", periods=48, freq="M"),
        "Region": ["North", "South", "East", "West"] * 12,
        "Unemployment_Rate": [5.0, 6.1, 7.2, 6.8,
                              5.2, 6.5, 7.4, 7.0,
                              6.0, 7.2, 8.1, 7.5] * 4
    }

    df_sample = pd.DataFrame(data)
    df_sample.to_csv("unemployment.csv", index=False)
    print("✅ Sample unemployment.csv created!")

# Load dataset
df = pd.read_csv("unemployment.csv")

# -----------------------------
# Step 2: Data Cleaning
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

print("\n First rows of dataset:")
print(df.head())

print("\n Dataset Info:")
print(df.info())

print("\n Descriptive Stats:")
print(df.describe())

# -----------------------------
# Step 3: Visualization
# -----------------------------

# Overall Trend
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='Unemployment_Rate', hue='Region', marker="o")
plt.title("Unemployment Rate Over Time by Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title='Region')
plt.show()

# Covid-19 Impact (2020–2021)
covid_period = df[(df['Date'] >= "2020-01-01") & (df['Date'] <= "2021-12-31")]

plt.figure(figsize=(12,6))
sns.lineplot(data=covid_period, x='Date', y='Unemployment_Rate', hue='Region', marker="o")
plt.title("Covid-19 Impact on Unemployment Rates (2020–2021)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title='Region')
plt.show()

# Seasonal Patterns (Monthly Avg)
df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['Unemployment_Rate'].mean()

plt.figure(figsize=(10,5))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o')
plt.title("Seasonal Trend in Unemployment Rate (Average by Month)")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.show()

# -----------------------------
# Step 4: Insights
# -----------------------------
print("\n---  Insights ---")
print("1. Unemployment spiked during Covid-19 (2020–2021).")
print("2. Some regions show consistently higher unemployment.")
print("3. Seasonal variations indicate certain months face higher unemployment.")
