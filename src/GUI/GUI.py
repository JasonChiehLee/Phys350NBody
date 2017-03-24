from tkinter import*
root = Tk()

desc = "The Odd Squad presents: 3 Body Orbital Mechanics"

w1 = Label(root,
    justify=LEFT, text=desc).grid(row=0, column=0, columnspan=2)

#logo = PhotoImage(file='./orbit_logo.gif')
#w2 = Label(root, image=logo).grid(row=0, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
mass_slider1 = Scale(root, from_=0, to= 1000,label="Mass 1",length=150,
    orient=HORIZONTAL)
mass_slider1.grid(row=2, column=0)

entry2 = Entry(root)
entry2.grid(row=1, column=1)
mass_slider2 = Scale(root, from_=0, to= 1000,label="Mass 2",length=150,
    orient=HORIZONTAL)
mass_slider2.grid(row=2, column=1)

entry3 = Entry(root)
entry3.grid(row=1, column=2)
mass_slider3 = Scale(root, from_=0, to= 1000,label="Mass 3",length=150,
    orient=HORIZONTAL)
mass_slider3.grid(row=2, column=2)


button = Button(root, text='QUIT', fg="red", command=quit)
button.grid(row=3, column=0)
root.mainloop()
