from tkinter import*
root = Tk()
root.wm_title("PHYS 350: 3 Body Orbital Mechanics")
desc = "The Odd Squad presents: 3 Body Orbital Mechanics"

description = Label(root,
    justify=LEFT, text=desc).grid(row=0, column=0, columnspan=2)

#logo = PhotoImage(file='./orbit_logo.gif')
#w2 = Label(root, image=logo).grid(row=0, column=1)
m1_label = Label(root, text="Mass 1").grid(row=1, column=0)
m1_entry = Entry(root)
m1_entry.grid(row=2, column=0)
m1_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
m1_slider.grid(row=3, column=0)

m2_label = Label(root, text="Mass 2").grid(row=1, column=1)
m2_entry = Entry(root)
m2_entry.grid(row=2, column=1)
m2_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
m2_slider.grid(row=3, column=1)

m3_label = Label(root, text="Mass 3").grid(row=1, column=2)
m3_entry = Entry(root)
m3_entry.grid(row=2, column=2)
m3_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
m3_slider.grid(row=3, column=2)

set_mass = Button(root, text='Set Mass')
set_mass.grid(row=4, column=1)

v1_label = Label(root, text="Velocity 1").grid(row=5, column=0)
v1_entry = Entry(root)
v1_entry.grid(row=6, column=0)
v1_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
v1_slider.grid(row=7, column=0)

v2_label = Label(root, text="Velocity 2").grid(row=5, column=1)
v2_entry = Entry(root)
v2_entry.grid(row=6, column=1)
v2_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
v2_slider.grid(row=7, column=1)

v3_label = Label(root, text="Velocity 3").grid(row=5, column=2)
v3_entry = Entry(root)
v3_entry.grid(row=6, column=2)
v3_slider = Scale(root, from_=0, to= 1000, length=150,
    orient=HORIZONTAL)
v3_slider.grid(row=7, column=2)

set_vel = Button(root, text='Set Velocity')
set_vel.grid(row=8, column=1)

quit_but = Button(root, text='QUIT', command=quit)
quit_but.grid(row=9, column=1)
root.mainloop()
