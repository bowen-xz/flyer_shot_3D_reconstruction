import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from flyer_shot_3Dreconstruct import model_displacement
import customtkinter as ctk


def button1_clicked():
    print("Button Clicked", "Button 1 was clicked!")

def button2_clicked():
    print("Button Clicked", "Button 2 was clicked!")

# Create the tkinter window
root = ctk.CTk()
root.title("Functional Buttons Example")

# Create buttons
button1 = ctk.CTkButton(root, text="Button 1", command=button1_clicked)
button1.pack(pady=10)

button2 = ctk.CTkButton(root, text="Button 2", command=button2_clicked)
button2.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
