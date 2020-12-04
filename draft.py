import pandas as pd 
import os
df = pd.read_csv('phq9.csv', header=0)
#print(df)
scores = df['total']
average = round(scores.mean(), 1)

#print(average)
print(scores[1])