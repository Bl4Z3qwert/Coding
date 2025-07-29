import tkinter as tk
from tkinter import ttk

# Function to convert cm to inches
def convert_cm_to_inch():
    try:
        cm = float(entry.get())
        inch = cm / 2.54
        result_label.config(text=f"{inch:.2f} inches")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create window
root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")
root.configure(bg="#f0f8ff")  # Optional background color

# Title label
title = tk.Label(root, text="Convert Centimeters to Inches", font=("Helvetica", 14), bg="#f0f8ff", fg="#333")
title.pack(pady=20)

# Entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_cm_to_inch, bg="#4CAF50", fg="white", font=("Arial", 12))
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#000")
result_label.pack(pady=10)

# Run app
root.mainloop()
