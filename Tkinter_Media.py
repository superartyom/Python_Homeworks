import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.title('Music Player')
window.geometry('480x260')
window.resizable(width=False, height=False)
window.configure(background='#FFFFFF')

txt = tkinter.StringVar(value='Nothing Plays')

Status = tkinter.Label(window, textvar=txt, font=('Helvetica', 15), borderwidth=1, relief='flat')
Status.grid(row=0, column=0, columnspan=4, sticky='ew')

Volume = ttk.Scale(window)
Volume.grid(row=1, column=0, columnspan=4, sticky='ew')

Play_Button = tkinter.Button(window, text='Play', font=('Helvetica', 10, 'bold'), width=10, height=2, relief='flat', borderwidth=1, background='#0fa621', activebackground='#0fa621')
Play_Button.grid(row=2, column=0, sticky='ew')

Pause_Button = tkinter.Button(window, text='Pause', font=('Helvetica', 10, 'bold'), width=10, height=2, relief='flat', borderwidth=1, background='#ff0000', activebackground='#ff0000')
Pause_Button.grid(row=2, column=1, sticky='ew')

Previous_Button = tkinter.Button(window, text='Previous song', font=('Helvetica', 10, 'bold'), width=10, height=2, relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
Previous_Button.grid(row=2, column=2, sticky='nsew')

Next_Button = tkinter.Button(window, text='Next song', font=('Helvetica', 10, 'bold'), width=10, height=2, relief='flat', borderwidth=1, background='#696764', activebackground='#696764')
Next_Button.grid(row=2, column=3, sticky='ew')

List = tkinter.Listbox(window)
List.grid(row=3, column=0, columnspan=4, sticky='nsew')

window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=2)
window.columnconfigure(2, weight=2)
window.columnconfigure(3, weight=2)
window.mainloop()
