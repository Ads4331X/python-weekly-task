"""
Program to read CSV data and create scatter plots using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

file_name = 'health_data.csv'
df = pd.read_csv(file_name) 


# color based on gender 
colors = df['gender'].map({'Male': 'blue', 'Female': 'red'})


# weight vs height scatter diagram
plt.scatter(df['weight'] , df['height'])
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Weight vs Height')
plt.show()


# age vs weight scatter diagram
plt.scatter(df['age'] , df['weight'])
plt.xlabel('Age')
plt.ylabel('Weight')
plt.title('Age vs Weight')
plt.show()

# height vs age scatter diagram
plt.scatter(df['height'] , df['age'])
plt.xlabel('Height')
plt.ylabel('Age')
plt.title('Height vs Age')
plt.show()

# gender vs height scatter diagram
plt.scatter(df['gender'] , df['height'] ,c=colors)
plt.xlabel('Gender (0=Male, 1=Female)')
plt.ylabel('Height')
plt.title('Gender vs Height')
plt.show()

# gender vs weight scatter diagram
plt.scatter(df['gender'], df['weight'] , c=colors)
plt.xlabel('Gender (0=Male, 1=Female)')
plt.ylabel('Weight')
plt.title('Gender vs Weight')
plt.show()