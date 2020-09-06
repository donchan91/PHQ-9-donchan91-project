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
    #__init__ method initialises the class. self if implied, and needs not be passed. First parameter in every Method. kwarg= key word arguments (e.g. in a dictionary)
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

        
        #Frame of the page. Main Canvas attaches here. 
        main_frame = tk.Frame(self)
        main_frame.grid_propagate(True)
        main_frame.grid()

        #Main Canvas. Scrollbar attaches here. 
        main_canvas = tk.Canvas(main_frame, scrollregion=(0, 0, 1200, 800))
        main_canvas.grid(row=0, column=0, sticky="nsew")
        main_canvas.grid_propagate(True)
       

        

        #Scrollbar
        scroll = tk.Scrollbar(self, orient="vertical", command=main_canvas.yview)
        
        scroll.grid(row=0, column=1, sticky="ns")        
        main_canvas.configure(yscrollcommand=scroll.set)

        


        title = tk.Label(main_canvas, text="PHQ-9 Questionnaire", pady=10, font=TITLE_FONT)
        title.grid(row=0, column=0, columnspan=5, sticky="w")
        q1t = tk.Label(main_canvas, text=q1, justify="left", font=LARGE_FONT)
        q1t.grid(row=1, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q1a, value = i, text=choice[i], justify="left").grid(row=(i+2), sticky="w") #end row = 5

        q2t = tk.Label(main_canvas, text=q2, justify="left")
        q2t.grid(row=6, column=0, columnspan=3, sticky="w") 
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q2a, value = i, text=choice[i], justify="left").grid(row=7 + i, sticky="w") #ends in row 10
       
        q3t = tk.Label(main_canvas, text=q3, justify="left")
        q3t.grid(row=11, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q3a, value = i, text=choice[i], justify="left").grid(row=(12 + i), column=0, sticky="w") #ends in row 15

        q4t = tk.Label(main_canvas, text=q4, justify="left")
        q4t.grid(row=16, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q4a, value = i, text=choice[i], justify="left").grid(row=(17 + i), sticky="w") #ends in 20

        q5t = tk.Label(main_canvas, text=q5, justify="left")
        q5t.grid(row=21, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q5a, value = i, text=choice[i], justify="left").grid(row=22 + i, sticky="w") #ends in row 25

        q6t = tk.Label(main_canvas, text=q6, justify="left")
        q6t.grid(row=26, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q6a, value = i, text=choice[i], justify="left").grid(row=27 + i, sticky="w")

        q7t = tk.Label(main_canvas, text=q7, justify="left")
        q7t.grid(row=31, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q7a, value = i, text=choice[i], justify="left").grid(row=32 + i, sticky="w")

        q8t = tk.Label(main_canvas, text=q8, justify="left")
        q8t.grid(row=36, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q8a, value = i, text=choice[i], justify="left").grid(row=37 + i, sticky="w")
 
        q9t = tk.Label(main_canvas, text=q9, justify="left")
        q9t.grid(row=41, column=0, columnspan=3, sticky="w")
        for i in range(0, 4):
            tk.Radiobutton(main_canvas, variable=q9a, value = i, text=choice[i], justify="left").grid(row=42 + i, sticky="w")

        #Getting width and height to automatically calibrate position of scroll bar
        window_width = main_canvas.winfo_reqwidth()
        window_height = main_canvas.winfo_reqheight()
        main_canvas.config(width=window_width, height=window_height)
        print(window_height)
        print(window_width)
       

app = MainBody()
app.geometry('1296x768')
app.mainloop()
