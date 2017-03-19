from tkinter import*
root = Tk()

desc = "The Odd Squad Presents: 3 Body Orbital Mechanics"

w1 = Label(root,
    justify=LEFT, padx = 10, text=desc).pack()

logo = PhotoImage(file='./orbit_logo.gif')
w2 = Label(root, image=logo).pack()

mass_slider1 = Scale(root, from_=0, to= 1000,label="Mass 1",length=150, orient=HORIZONTAL)
mass_slider1.pack()

mass_slider2 = Scale(root, from_=0, to= 1000,label="Mass 2",length=150, orient=HORIZONTAL)
mass_slider2.pack()

mass_slider3 = Scale(root, from_=0, to= 1000,label="Mass 3",length=150, orient=HORIZONTAL)
mass_slider3.pack()


button = Button(root, text='QUIT', fg="red", command=quit)
button.pack()
root.mainloop()
