import tkinter as tk
from tkinter import Frame, Label, Button, StringVar, IntVar, Tk
import pandas as pd
import csv
import os
from subprocess import call

#Loading phq9.csv or creating a new file
if os.path.isfile('phq9.csv'):
    df = pd.read_csv('phq9.csv', header=0)
else:
    headers = ['date', 'time', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total', 'severity']
    df = pd.DataFrame(columns = headers)
    df.to_csv('phq9.csv', index = False)
    df = pd.read_csv('phq9.csv', header=0)

main_window = Tk() #Required as the whole body of the app. Acts as a frame
main_window.title("Mental Health Tracker")

paragraph_one = StringVar()
paragraph_one.set("This is the PHQ-9 questionnaire.\nPlease choose from the following options. \nPLEASE NOTE: This is NOT used as a diagnostic tool for depression and related disorders.\n Should there be genuine concerns about the mental well-being of you or someone you know, \nyou should consult a medical professional for their assessment and/or treatment.")


#canvas = tk.Canvas(window, height = 700, width = 700, bg='#CBD0E1')
#canvas.pack() #This attaches the canvas into the window
Label(main_window, justify="left", textvariable=paragraph_one).pack()


phq9 = Frame(main_window)

def answer_phq9():
    import phq9

Button(text="Answer PHQ-9", command = answer_phq9).pack()
Button(text="Display Data").pack()








main_window.mainloop()  #Displays main GUI