from tkinter import *

phone = Tk()

phone.geometry('400x500')

name = StringVar()
no = StringVar()

fr = Frame()
fr.pack(pady=10)

fr1 = Frame()
fr1.pack()

fr2 = Frame()
fr2.pack(pady=10)

Label(fr, text = 'Name', font='arial 12 bold').pack(side=LEFT)
Entry(fr, textvariable = name,width=50).pack()

Label(fr1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT)
Entry(fr1, textvariable = no,width=50).pack()

Label(fr2, text = 'Address', font='arial 12 bold').pack(side=LEFT)
add = Text(fr2,width=37,height=10)
add.pack()

Button(phone,text="Add",font="arial 12 bold").place(x= 100, y=270)
Button(phone,text="View",font="arial 12 bold").place(x= 100, y=310)
Button(phone,text="Delete",font="arial 12 bold").place(x= 100, y=350)
Button(phone,text="Reset",font="arial 12 bold").place(x= 100, y=390)

scroll_bar = Scrollbar(phone, orient=VERTICAL)
select = Listbox(phone, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

phone.mainloop()