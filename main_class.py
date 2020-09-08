import tkinter as tk
from tkinter import Frame, Label,  Tk, StringVar, IntVar, ttk, Text, BooleanVar
from datetime import datetime
from text import *
import pandas as pd 
import os 



TITLE_FONT = ("Verdana", 24)
LARGE_FONT = ("Verdana", 12)

#Imports phq9.csv if file is located within the local directory.
if os.path.isfile('phq9.csv'):
    df = pd.read_csv('phq9.csv', header=0)
else:
    headers = ['date', 'time', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'total', 'severity']
    df = pd.DataFrame(columns = headers)
    df.to_csv('phq9.csv', index = False)
    df = pd.read_csv('phq9.csv', header=0)

#
class MainBody(tk.Tk):
    #__init__ method initialises the class.  First parameter in every Method. kwarg= key word arguments (e.g. in a dictionary)
    def __init__(self, *args, **kwargs):
        #Initialise 
        tk.Tk.__init__(self, *args, *kwargs) #Initialising Tkinter
        #Creating a container to populate within initialisation function
        tk.Tk.wm_title(self, "Mental Wellbeing Toolkit by donchan91")
        container = tk.Frame(self) #Frame is a window edge. 
        container.pack(side="top", fill="both", expand=True) #Fill will fill in the space allotted in the pack. Expand will expand across the whitespace in the screen. 
        container.grid_rowconfigure(0, weight=1) #Part of tkinter.Tk. 0 is the minimum size. Weight is the priority setting.
        container.grid_columnconfigure(0, weight=1)
        self.frames = {} #All the frames will be stored here. 
        for F in (StartPage, phq9_intro, phq9_main):
            frame = F(container, self) #will define this later on.
            self.frames[F] = frame #
            frame.grid(row=0, column = 0, sticky="nsew") #sticky="nsew" defines alignment and stretch. nsew refers to north, south, east, west. 
        self.show_frame(StartPage)

    def show_frame(self, cont): #Method to display frame
        frame = self.frames[cont]
        frame.tkraise() #tkraise will raise the screeen to the front. 

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        heading = tk.Label(self, text="Mental Health Toolkit", font=TITLE_FONT)
        heading.grid(row=0, column=0, pady=10, padx=10) 
        #Paragraph below
        description = tk.Text(self, height=5, width=100, wrap="word", borderwidth=0)
        description.insert(tk.END, main_intro)#PARAGRAPH
        description.configure(state="disabled")
        description.grid(row=1, column=0,  padx=10, pady=10, columnspan=2)
        #Frames for Buttons for the Test
        button_frame = tk.Frame(self, padx=5, pady=5, borderwidth=1, relief="sunken")
        button_frame.grid(row=3, column=0, columnspan=3, sticky="W")
        label_03 = tk.Label(self, text="Take Assessments", justify="left")
        label_03.grid(row=2, column=0, sticky="W")        
        button1 = ttk.Button(button_frame, text="Answer PHQ-9", command = lambda: controller.show_frame(phq9_intro))
        button1.grid(row=2, column=0)
        button2 = ttk.Button(button_frame, text="HAD Anxiety Test")
        button2.grid(row=2, column=1)
        #Frames for Buttons to display results

class phq9_intro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Title
        label = tk.Label(self, text="PHQ-9 Questionnaire", font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=3 ,padx=10, pady=10)
        #Description
        phq9_intro = tk.Text(self, height=10, width=100, wrap="word", borderwidth=0)
        phq9_intro.insert(tk.END, phq_description)
        phq9_intro.configure(state="disabled")
        phq9_intro.grid(row=1, column=0,  padx=10, pady=10, columnspan=2)
        #Buttons
        disclaimer_button = tk.Button(self, text="Start", command = lambda: controller.show_frame(phq9_main))
        disclaimer_button.grid(row=5, column=1)


        button1 = tk.Button(self, text="Back to Main", command = lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=0)        
   
class phq9_main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Initialising variables which hold answers 
        q1a = IntVar()
        q2a = IntVar()
        q3a = IntVar()
        q4a = IntVar()
        q5a = IntVar()
        q6a = IntVar()
        q7a = IntVar()
        q8a = IntVar()
        q9a = IntVar()   

        phq9_body = tk.Frame(self)
        phq9_body.pack(fill="both", expand=1)

        #Canvas for the questionnaire
        phq9_canvas = tk.Canvas(phq9_body)
        phq9_canvas.pack(side="left", fill="both", expand=1)

        #Scrollbar
        scroll = ttk.Scrollbar(phq9_body, orient="vertical", command=phq9_canvas.yview)       
        scroll.pack(side='right', fill='y')

        #Configure canvas
        phq9_canvas.configure(yscrollcommand=scroll.set)
        phq9_canvas.bind('<Configure>', lambda e: phq9_canvas.configure(scrollregion = phq9_canvas.bbox('all')))


        #phqq_frame
        phq9_frame = tk.Frame(phq9_canvas)
        phq9_canvas.create_window((0,0), window=phq9_frame, anchor='nw')

        title = tk.Label(phq9_frame, text="PHQ-9 Questionnaire", pady=10, font=TITLE_FONT)
        title.grid(sticky="w")
        q1t = tk.Label(phq9_frame, text=q1, justify="left", font=LARGE_FONT)
        q1t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q1a, value = i, text=choice[i], justify="left").grid(sticky="w") #end row = 5

                        
        q2t = tk.Label(phq9_frame, text=q2, justify="left")
        q2t.grid(sticky="w") 
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q2a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 10
       
        q3t = tk.Label(phq9_frame, text=q3, justify="left")
        q3t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q3a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 15

        q4t = tk.Label(phq9_frame, text=q4, justify="left")
        q4t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q4a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in 20

        q5t = tk.Label(phq9_frame, text=q5, justify="left")
        q5t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q5a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 25

        q6t = tk.Label(phq9_frame, text=q6, justify="left")
        q6t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q6a, value = i, text=choice[i], justify="left").grid(sticky="w")

        q7t = tk.Label(phq9_frame, text=q7, justify="left")
        q7t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q7a, value = i, text=choice[i], justify="left").grid(sticky="w")

        q8t = tk.Label(phq9_frame, text=q8, justify="left")
        q8t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q8a, value = i, text=choice[i], justify="left").grid(sticky="w")
 
        q9t = tk.Label(phq9_frame, text=q9, justify="left")
        q9t.grid(sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(phq9_frame, variable=q9a, value = i, text=choice[i], justify="left").grid(sticky="w")

        #Getting width and height to automatically calibrate position of scroll bar
        window_width = 600
        window_height = 600
        self.config(width=window_width, height=window_height)
        #phq9_canvas.config(width=window_width, height=window_height)
        print(window_height)
        print(window_width)
        phq9_canvas.config(scrollregion=phq9_canvas.bbox('all'))

app = MainBody()
app.geometry('800x800')
app.mainloop()
