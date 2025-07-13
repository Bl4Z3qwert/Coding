# from tkinter import*


# window=Tk()
# window.title('Message box')
# window.geometry('188x188')
# def handle_keypress(event):
#     """Print character associted with keypress"""
#     print(event.char)
# window.bind('<Key>', handle_keypress)
# def handle_click(event):
#     print('The button was clicked')
# button=Button(window, text='Click me ')        
# button.pack()
# button.bind('<Button-1>', handle_click)
# window.mainloop() 




from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('200x200')
def warning():
    messagebox.showinfo('Message', "this is a message box")
    messagebox.showwarning('Message', 'this is a warning')


button=Button(root, text='Show message ',command=warning)    
button.place(x=40, y=80)  
root.mainloop()