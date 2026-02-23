#Logan Miranowski
#CSCI601_Avanced_Programming_with_Python
#Mini-Project 2

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('spending_patterns_detailed.csv')

streaming_df = df[(df["Category"] == "Subscription") & 
                  (df["Type"] == "Streaming Service")]

streaming_customers = streaming_df["CustomerID"].nunique()
total_customers = df["CustomerID"].nunique()

percentage = (streaming_customers / total_customers) * 100

print(f"Percentage of customers who subscribe to streaming services: {percentage:.2f}%")

# Create charts folder if it doesn't exist
if not os.path.exists('charts'):
    os.makedirs('charts')

# Prepare data
labels = ["Streaming Subscribers", "Non-Subscribers"]
values = [streaming_customers, total_customers - streaming_customers]

#create chart
plt.figure(figsize=(8,6))
plt.bar(labels, values)
plt.title("Customer Subscription to Streaming Services")
plt.ylabel("Number of Customers")
plt.xlabel("Customer Type")
plt.grid(axis='y')

# save the chart
plt.savefig('charts/streaming_subscription_chart.png')
plt.close()