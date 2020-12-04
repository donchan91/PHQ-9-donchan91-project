#Note: THis file is used only to test new code 

from datetime import datetime
from time import strftime
from statistics import mean
import numpy as np
import pandas as pd
import csv
import os.path

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
start = True
#Read .csv into a DataFrame or create new savefile
if os.path.isfile('phq9.csv'):
    df = pd.read_csv('phq9.csv', header=0)
else:
    headers = ['date', 'time', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total', 'severity']
    df = pd.DataFrame(columns = headers)
    df.to_csv('phq9.csv', index = False)
    df = pd.read_csv('phq9.csv', header=0)

#print(df['date'])

print(df['date'])


print(len(df)) #Returned the correct length 4

#For loop below will iterate through the dates, and return True if there are duplicates
def check_duplicate():
    for i in range(len(df) - 1):
        print(df['date'][i] == df['date'][i + 1]) #This returns if there are duplicate entries

def sort_out_duplicate():
    display_df = pd.DataFrame({})
    for i in range(len(df) - 1):
        #Loop through with the criteria that if they 
        if df['date'][i] == df['date'][i + 1]:
            pass #Put code about getting the highest score
        else:
            pass