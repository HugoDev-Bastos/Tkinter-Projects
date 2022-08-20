from tkinter import *


app = Tk()
app.title("CFB cursos")
app.geometry("500x300")
app.configure(background="#008")

txt1 = Label(app, text="Curso de Python!", background="#ff0", foreground="#000")
txt1.place(x=10, y=10, width=150, height=30)

vtxt="Módulo Tkinter"
vbg="#008"
vfg="#fff"

txt2= Label(app, text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=5, padx=5, pady=5, side="top", fill="x", expand=True )
app.mainloop()
