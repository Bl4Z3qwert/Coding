import tkinter as tk
import re


def check_strength():
    password = entry.get()
    strength = "Weak"
    color = "red"

    if len(password) < 6:
        strength = "Too Short"
        color = "gray"
    elif re.search(r"[A-Z]", password) and \
         re.search(r"[a-z]", password) and \
         re.search(r"\d", password) and \
         re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) and \
         len(password) >= 8:
        strength = "Strong"
        color = "green"
    elif re.search(r"[A-Za-z]", password) and re.search(r"\d", password):
        strength = "Medium"
        color = "orange"

    result_label.config(text=f"Strength: {strength}", fg=color)


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")


tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)


entry = tk.Entry(root, show="*", width=30)
entry.pack()


tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)
 
 
 
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()


root.mainloop()
