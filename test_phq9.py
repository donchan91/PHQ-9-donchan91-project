import tkinter as tk
from tkinter import Frame, Label,  Tk, StringVar, IntVar, ttk, Text, BooleanVar
from datetime import datetime
from text import *
import pandas as pd 
import os 
   
TITLE_FONT = ("Verdana", 24)
LARGE_FONT = ("Verdana", 12)

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

q1a = IntVar()
q2a = IntVar()
q3a = IntVar()
q4a = IntVar()
q5a = IntVar()
q6a = IntVar()
q7a = IntVar()
q8a = IntVar()
q9a = IntVar()

label1 = tk.Label(frame_main, text="Label 1", fg="green")
label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

label2 = tk.Label(frame_main, text="Label 2", fg="blue")
label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

label3 = tk.Label(frame_main, text="Label 3", fg="red")
label3.grid(row=3, column=0, pady=5, sticky='nw')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
canvas_frame = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

# Add 9-by-5 buttons to the frame
q1t = tk.Label(canvas_frame, text=q1, justify="left", font=LARGE_FONT)
q1t.pack(anchor="w")
for i in range(0, 4):
    tk.Radiobutton(canvas_frame, variable=q1a, value = i, text=choice[i], justify="left").pack(anchor="w")


# Update buttons frames idle tasks to let tkinter calculate buttons sizes
canvas_frame.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
#first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
#first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
#frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                    #height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()