import tkinter as tk
import numpy as np
import os

# setting up the basic interface

root = tk.Tk()

root.title("Daily reminder")

canvas = tk.Canvas(root,height=500,width=500)
canvas.pack()

frame = tk.Frame(root,bg='white')
frame.place(relwidth=1.0,relheight=1.0)

# setting up functions

things = []

def display(thing_list):
    number = 1
    for thing in thing_list:
        label = tk.Label(frame,text=str(number)+":"+" "+thing)
        label.pack()
        number+=1

def clear_labels():
    wlist = frame.winfo_children()
    part_list = wlist[1:]
    for widget in part_list:
        widget.destroy()

# first try to load up the saved texts

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        temp_things = f.read()
        temp_things = temp_things.split(",")
        things = [x for x in temp_things if x.strip()]

def add_things():
    
    # first clear up the mess created on the last loop
    
    clear_labels()

    # then add the new thing and display it
    
    thing = entry1.get()
    things.append(thing)
    
    # clearing the entry box
    
    entry1.delete(0,"end")
    
    display(things)

def clear():
    if os.path.isfile('save.txt'):
        os.remove('save.txt')
        things.clear()
        clear_labels()
        display(things)
        

# setting up the buttons and entries

entry1 = tk.Entry(root,bg='skyblue')
canvas.create_window(260, 368, window=entry1)
label1 = tk.Label(frame,text="Add a new to-do:")
label1.place(x=207, y=320)

Add_button = tk.Button(root,text="Add!", padx=15, pady=10, fg = "white", bg="green",command = add_things)
Add_button.place(x=220,y=400)

Clear_button = tk.Button(root,text="Clear!", padx=15, pady=10, fg = "white", bg="green", command = clear)
Clear_button.place(x=217,y=450)

# display the saved ones

display(things)


root.mainloop()

# saving the things to do 

if(things):
    with open('save.txt','w') as f:
        for thing in things:
            f.write(thing+',')

