from Tkinter import*
root = Tk()
logo = PhotoImage(file='./orbit_logo.gif')
w1 = Label(root, image=logo).pack(side="right")
button = Button(root, text='QUIT', fg="red", command=quit)
button.pack(side=BOTTOM)
desc = "The Odd Squad Presents: 3 Body Orbital Mechanics"

w2 = Label(root,
    justify=LEFT, padx = 10, text=desc).pack(side="left")
root.mainloop()
