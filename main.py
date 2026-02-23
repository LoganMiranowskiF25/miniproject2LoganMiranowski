#Logan Miranowski
#CSCI601_Avanced_Programming_with_Python
#Mini-Project 2

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('spending_patterns_detailed.csv')

print(df.columns)
print(df.head())

streaming_df = df[(df["Category"] == "Subscription") & 
                  (df["Type"] == "Streaming Service")]

streaming_customers = streaming_df["CustomerID"].nunique()
total_customers = df["CustomerID"].nunique()

percentage = (streaming_customers / total_customers) * 100

print(f"Percentage of customers who subscribe to streaming services: {percentage:.2f}%")