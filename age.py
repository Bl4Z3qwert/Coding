import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())

        today = date.today()
        age = today.year - birth_year

        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1

        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for day, month, and year.")


root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
root.resizable(False, False)


tk.Label(root, text="Enter Your Birth Date", font=("Arial", 14)).pack(pady=10)


tk.Label(root, text="Day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()


tk.Label(root, text="Month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()


tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()


tk.Button(root, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white").pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run the GUI
root.mainloop()