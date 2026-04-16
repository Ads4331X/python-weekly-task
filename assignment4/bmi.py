"""
Program to calculate BMI and classify health status from CSV data.
"""

import pandas as pd

df = pd.read_csv("health_data.csv")

# calculate BMI (height converted from cm to meters)
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)

# function to get health status based on BMI
def get_health_status(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Healthy range'
    elif 25 <= bmi <= 29.9:
        return 'Overweight risk'
    elif 30 <= bmi <= 34.9:
        return 'High risk of diabetes/heart disease'
    elif bmi >= 40:
        return 'Critical health condition'
    else:
        return 'Severely Obese'  

df['Health_Status'] = df['BMI'].apply(get_health_status)

print(df)