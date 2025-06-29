from tkinter import  *
from datetime import date
root=Tk()
root.title('Welcome to tkinter')
root.geometry('400x300')
lab=Label(text='Hello wecome!!!', fg='blue',bg='#0083a1', height=1,width=300)
name_lab=Label(text='Full name', bg= '#7758d3')
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message= "Welcome \n Today's date is:"  + str(date.today()) + "\n Hello" + name + "!"
    greet='Hello' + name + '!\n'
    
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
    
    
    
text_box=Text(height=3)   
but=Button (text='Begin', command=display,height=1, bg='#768586', fg='white') 
lab.pack()
name_lab.pack()
name_entry.pack()
but.pack()
text_box.pack()
root.mainloop()