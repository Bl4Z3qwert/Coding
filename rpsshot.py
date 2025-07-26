import tkinter as tk
import random


def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")


root = tk.Tk()
root.geometry("400x400")
root.title("Rock,Paper and Scissors")  


instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 14))
instruction.pack(pady=20)


button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)


result_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
result_label.pack(pady=30)


root.mainloop()
