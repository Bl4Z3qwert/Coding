import tkinter as tk


def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())


        si = (p * t * r) / 100

        
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}", fg="#006400")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.", fg="red")


root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")  # As per instruction


label_color = "#333"
entry_bg = "#f0f0f0"
bg_color = "#d3e0ea"

root.configure(bg=bg_color)


tk.Label(root, text="Principal (₹):", bg=bg_color, fg=label_color).grid(row=0, column=0, padx=10, pady=10, sticky="e")
principal_entry = tk.Entry(root, bg=entry_bg)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Time (years):", bg=bg_color, fg=label_color).grid(row=1, column=0, padx=10, pady=10, sticky="e")
time_entry = tk.Entry(root, bg=entry_bg)
time_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Rate (%):", bg=bg_color, fg=label_color).grid(row=2, column=0, padx=10, pady=10, sticky="e")
rate_entry = tk.Entry(root, bg=entry_bg)
rate_entry.grid(row=2, column=1, padx=10, pady=10)


tk.Button(root, text="Calculate Interest", command=calculate_interest, bg="#4caf50", fg="white").grid(row=3, columnspan=2, pady=20)


result_label = tk.Label(root, text="", bg=bg_color, font=("Arial", 12))
result_label.grid(row=4, columnspan=2)


root.mainloop()
