import customtkinter as ctk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from flyer_shot_3Dreconstruct import model_displacement, model_velocity

#If putton clicked functions
def displacement_button_clicked():
    print("Button Clicked", "Button Displacement was clicked!")
    path0 = textbox_path0.get()
    path1 = textbox_path1.get()
    path2 = textbox_path2.get()
    path3 = textbox_path3.get()
    model_displacement(path0, path1, path2, path3)

def velocity_button_clicked():
    print("Button Clicked", "Button Velocity was clicked!")
    path0 = textbox_path0.get()
    path1 = textbox_path1.get()
    path2 = textbox_path2.get()
    path3 = textbox_path3.get()
    model_velocity(path0, path1, path2, path3)


# Create the main window
root = ctk.CTk()
root.title("PDV 3D Reconstruction")
root.geometry("600x400")

# Set the appearance mode of customtkinter (optional)
ctk.set_appearance_mode("System")  # "Light", "Dark", "System"

# Create a frame to center the widgets
frame = ctk.CTkFrame(root)
frame.pack(expand=True, fill='both', padx=10, pady=10)

# Create the title label
title_label = ctk.CTkLabel(frame, text="PDV 3D Reconstruction", font=("Arial", 20))
title_label.pack(pady=(20, 10))  # Add more padding on the top

# Create containers for each row of textboxes and labels
row_containers = []



#CSV file path textbox0
row_frame = ctk.CTkFrame(frame)
row_frame.pack(pady=5)

"""    
textbox_x = ctk.CTkEntry(row_frame, width=80, placeholder_text="x location")
textbox_x.pack(side='left', padx= 5)

textbox_y = ctk.CTkEntry(row_frame, width=80, placeholder_text="y location")
textbox_y.pack(side='left', padx= 5)
"""

textbox_path0 = ctk.CTkEntry(row_frame, width=300, placeholder_text="CSV File Path")
textbox_path0.pack(side='left', padx= 5)

row_containers.append(row_frame)


#CSV file path textbox1
row_frame = ctk.CTkFrame(frame)
row_frame.pack(pady=5)

textbox_path1 = ctk.CTkEntry(row_frame, width=300, placeholder_text="CSV File Path")
textbox_path1.pack(side='left', padx= 5)

row_containers.append(row_frame)


#CSV file path textbox2
row_frame = ctk.CTkFrame(frame)
row_frame.pack(pady=5)

textbox_path2 = ctk.CTkEntry(row_frame, width=300, placeholder_text="CSV File Path")
textbox_path2.pack(side='left', padx= 5)

row_containers.append(row_frame)

#CSV file path textbox3
row_frame = ctk.CTkFrame(frame)
row_frame.pack(pady=5)

textbox_path3 = ctk.CTkEntry(row_frame, width=300, placeholder_text="CSV File Path")
textbox_path3.pack(side='left', padx= 5)

row_containers.append(row_frame)




# Create a frame for the buttons to align them horizontally
button_frame = ctk.CTkFrame(frame)
button_frame.pack(pady=20)

# Create the "Model Displacement" button
displacement_button = ctk.CTkButton(button_frame, text="Model Displacement", command=displacement_button_clicked)
displacement_button.pack(side='left', padx=10)

# Create the "Model Velocity" button
velocity_button = ctk.CTkButton(button_frame, text="Model Velocity", command=velocity_button_clicked)
velocity_button.pack(side='left', padx=10)

# Run the main event loop
root.mainloop()
