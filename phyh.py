from tkinter import *

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box = Entry(2)
        result_box.delete(0, END)
        result_box.insert(0, str(product))
    except ValueError:
        result_box.delete(0, END)
        result_box.insert(0, "Invalid input")

app = Tk()
app.geometry("400x300")
app.title("Getting Started with Widgets")

label_intro = Label(app, text="This app multiplies two numbers")
label_intro.pack(pady=5)

label1 = Label(app, text="Enter first number:")
label1.pack()

entry1 = Entry(app)
entry1.pack(pady=5)
