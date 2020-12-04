import tkinter as tk
from tkinter import Tk, ttk, IntVar
from text import *

root = Tk()
root.geometry("500x400")
root.title('Scroll Practice')
q1a = IntVar()
q2a = IntVar()
q3a = IntVar()
q4a = IntVar()
q5a = IntVar()
q6a = IntVar()
q7a = IntVar()
q8a = IntVar()
q9a = IntVar() 
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=1)

#Create a canvas
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side="left", fill="both", expand=1)

#Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview) #Put into main_frame, set the yscroll to the canvas
my_scrollbar.pack(side="right", fill="y")

#Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

#ANOTHER frame inside the canvas
second_frame  = tk.Frame(my_canvas)

#Add second_frame to a window within the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw") #Set cordinates, window is the frame you want, and anchor is the location

#Test: 
q1t = tk.Label(second_frame, text=q1, justify="left")
q1t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q1a, value = i, text=choice[i], justify="left").grid(sticky="w") 

q2t = tk.Label(second_frame, text=q2, justify="left")
q2t.grid(sticky="w") 
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q2a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 10

q3t = tk.Label(second_frame, text=q3, justify="left")
q3t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q3a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 15

q4t = tk.Label(second_frame, text=q4, justify="left")
q4t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q4a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in 20

q5t = tk.Label(second_frame, text=q5, justify="left")
q5t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q5a, value = i, text=choice[i], justify="left").grid(sticky="w") #ends in row 25

q6t = tk.Label(second_frame, text=q6, justify="left")
q6t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q6a, value = i, text=choice[i], justify="left").grid(sticky="w")

q7t = tk.Label(second_frame, text=q7, justify="left")
q7t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q7a, value = i, text=choice[i], justify="left").grid(sticky="w")

q8t = tk.Label(second_frame, text=q8, justify="left")
q8t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q8a, value = i, text=choice[i], justify="left").grid(sticky="w")

q9t = tk.Label(second_frame, text=q9, justify="left")
q9t.grid(sticky="w")
for i in range(0, 4):
    tk.Radiobutton(second_frame, variable=q9a, value = i, text=choice[i], justify="left").grid(sticky="w")

root.mainloop()