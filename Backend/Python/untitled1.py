import pandas as pd
from tkinter import *
Phonebook = Tk()
Phonebook.geometry("1200x700")
Phonebook.title('Phonebook')

name = Label(Phonebook, text = 'Name : ', font = ('Arial',18,''))
name.place(x=350,y=100)
n=StringVar()
nEntry= Entry(Phonebook, width=30, font=("Arial",18,""), textvariable=n) 
nEntry.place(x=470,y=100) 

phno = Label(Phonebook, text = 'Phone : ', font = ('Arial',18,''))
phno.place(x=350,y=200)
p=StringVar()
pEntry= Entry(Phonebook, width=30, font=("Arial",18,""), textvariable=p) 
pEntry.place(x=470,y=200) 

phno2 = Label(Phonebook, text = 'Phone 2 : ', font = ('Arial',18,''))
phno2.place(x=350,y=300)
p2=StringVar()
p2Entry= Entry(Phonebook, width=30, font=("Arial",18,""), textvariable=p2) 
p2Entry.place(x=470,y=300) 

add = Label(Phonebook, text = 'Address : ', font = ('Arial',18,''))
add.place(x=350,y=400)
a=StringVar()
aEntry= Entry(Phonebook, width=30, font=("Arial",18,""), textvariable=a) 
aEntry.place(x=470,y=400) 

def save():
    a=0    
sbtn = Button(Phonebook, text='Save', width=20, height= 3, command=save)
sbtn.place(x=440,y=500)
def reset():
    a=0
rsbtn = Button(Phonebook, text='Reset', width=20, height= 3, command=reset)
rsbtn.place(x=620,y=500)

mainloop()