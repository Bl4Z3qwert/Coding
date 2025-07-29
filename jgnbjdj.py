import tkinter as tk

# Function to multiply the numbers
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"The product is: {result}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Multiply Two Numbers")
root.geometry("300x200")

# Labels and Entry widgets
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button to calculate product
multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.pack()

# Text widget to show result
result_text = tk.Text(root, height=2, width=30)
result_text.pack()

# Run the application
root.mainloop()
