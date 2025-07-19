import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self,root):
        self.root=root
        self.root.title(
            'Restaurant Management app'
        )
        self.menu_item={
            'Chips':2,
            'Bevarage':5,
            'Sushi':10,
            'Ramen':2.4
        }
        
        self.exchange_rate=82

        self.setup_background(root)

        frame=ttk.Frame(root)

        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)


        ttk.Label(frame,

        text="Restaurant Order Management",

        font=("Arial", 20, "bold")).grid(row=0,

        columnspan=3,

        padx=10,

        pady=10

        )
        self.menu_labels={}
        self.menu_qualities={}
        for i,(item,price) in enumerate(self.menu_item.items(),start=1):
            label=ttk.Label(
                frame,
                text=f'{item} (${price}):'
                font=('Arial',12)
            )
            
