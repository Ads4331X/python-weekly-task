"""
Program to calculate BMI and classify health status from CSV data.
"""

import pandas as pd

df = pd.read_csv("health_data.csv")

df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2) # calculate BMI 

# function to get health status 
def get_health_status(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi <= 24.9:
        return 'Healthy range'
    elif bmi <= 29.9:
        return 'Overweight risk'
    elif bmi <= 34.9:
        return 'High risk of diabetes/heart disease'
    else:
        return 'Critical health condition'

df['Health_Status'] = df['BMI'].apply(get_health_status)

print(df)

