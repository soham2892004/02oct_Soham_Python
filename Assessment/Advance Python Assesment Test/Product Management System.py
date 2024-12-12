import tkinter

Screen=tkinter.Tk()
Screen.geometry('475x250')
Screen.title("Registration Form")
Screen.config(bg='skyblue')
tkinter.Label(text='Product Manager',bg='orange',fg='black',font='Stencil').grid(row=0,column=3,sticky='n')
tkinter.Button(text='Register',bg='navy',fg='green',font='Stencil').grid(row=3,column=3,sticky='n')
tkinter.Button(text='log in',bg='pink',fg='Maroon',font='Stencil').grid(row=6,column=3,sticky='n')

tkinter.Button(text='Manage Stock',bg='yellow',fg='purple',font='Stencil').grid(row=10,column=3,sticky='n')
tkinter.Button(text='View Stock',bg='yellow',fg='purple',font='Stencil').grid(row=12,column=3,sticky='n')

tkinter.Label(text='Customer',bg='orange',fg='black',font='Stencil').grid(row=0,column=15,sticky='s')
tkinter.Button(text='Register',bg='navy',fg='green',font='Stencil').grid(row=3,column=15,sticky='s')
tkinter.Button(text='log in',bg='pink',fg='Maroon',font='Stencil').grid(row=6,column=15,sticky='s')

tkinter.Button(text='Purchase Stock',bg='orange',fg='lightblue',font='Stencil').grid(row=10,column=15,sticky='s')
tkinter.Button(text='View Orders',bg='orange',fg='lightblue',font='Stencil').grid(row=12,column=15,sticky='s')

Screen.mainloop()