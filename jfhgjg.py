from tkinter import *
root = Tk()
root.geometry('400x300')
root.title('main')
def topwin():
  top =Toplevel()
  top.geometry('100x100')
  top.title('toplevel')
  l2=Label(top,text='The top level window')
  l4=Entry(top,text='the level name')
  l2.pack()
  l4.pack()
  top.mainloop()
  
l =Label(root,text= 'This is the root window')  
btn=Button(root,text='Click to open a new window', command=topwin)
l.pack()
btn.pack()
root.mainloop()