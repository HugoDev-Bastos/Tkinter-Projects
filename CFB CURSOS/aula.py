from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if vid.get() == "" or vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="Error", message="digite todos os dados!")
        return
    tv.insert("", "end", values=(vid.get(), vnome.get(), vfone.get()))
    vid.delete(0, END)
    vnome.delete(0, END)
    vfone.delete(0, END)
    vid.focus()
    
def deletar():
    print()
    
def consultar():
    print()
    
    
app = Tk()
app.title("")

## Label e Campos de Entrada

lbid = Label(app, text="ID", anchor=W)
vid = Entry(app)

lbnome = Label(app, text="Nome", anchor=W)
vnome = Entry(app)

lbfone = Label(app, text="Telefone", anchor=W)
vfone = Entry(app)

## TrenView

tv = ttk.Treeview(app, columns=("id", "nome", "telefone"), show="headings")
tv.column("id", minwidth=0, width=50)
tv.column("nome", minwidth=0, width=250)
tv.column("telefone", minwidth=0, width=100)
tv.heading("id", text="ID")
tv.heading("nome", text="Nome")
tv.heading("telefone", text="Telefone")

## Butão Inserir, Deletar e Consultar
btn_inserir = Button(app, text="Inserir", command=inserir)
btn_deletar = Button(app, text="Deletar", command=deletar)
btn_consultar = Button(app, text="Consultar", command=consultar)

## Organização do GRID do Widgtes

lbid.grid(column=0, row=0, sticky="w")
vid.grid(column=0, row=1)

lbnome.grid(column=1, row=0, sticky="w")
vnome.grid(column=1, row=1)

lbfone.grid(column=2, row=0, sticky="w")
vfone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_consultar.grid(column=2, row=4)

app.mainloop()