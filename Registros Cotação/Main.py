from ast import Delete
from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import left
import gerenciadorDB

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM clientes order by cod"
    linhas = gerenciadorDB.dql(vquery)
    for i in linhas:
        tv.insert("","end", values=i)

def inserir():
    if vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="Error", message="Digite todos os dados!")
        return
    try:
        vquery="INSERT INTO nome_cliente (nome, telefone) VALUES ("+vnome.get()+","+vfone.get()+")"
        gerenciadorDB.dml(vquery)
    except:
        messagebox.showinfo(title="Error", message="Erro ao inserir!")
        return
    popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vnome.focus()
    
def deletar():
    vid = -1
    itemSelecionado = tv.selection()[0]
    valores = tv.item(itemSelecionado, "values")
    vid = valores[0]
    try:
        vquery = " DELETE FROM clientes WHERE id="+vid
        gerenciadorDB.dml(vquery)
    except:
        messagebox.showinfo(title="Error", message="Erro ao deletar")
        return
    tv.delete(itemSelecionado)


def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM clientes WHERE nome_cliente LIKE '%" + vnomepesquisar.get()+ "%'"
    linhas = gerenciadorDB.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)    
    
app = Tk()
app.title("")


## TrenView
quadroGrid = LabelFrame(app, text="Registros")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=("id", "produto", "telefone"), show="headings")
tv.column("id", minwidth=0, width=50,)
tv.column("produto", minwidth=0, width=150)
tv.column("telefone", minwidth=0, width=100)

tv.heading("id", text="ID")
tv.heading("produto", text="Produto")
tv.heading("telefone", text="Telefone")
tv.pack()
popular()

## LabelFrame, Label, Entry, Button  => INSERIR CONTATOS
quadroInserir = LabelFrame(app, text="Inserir Novos Contatos")
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)

lbnome = Label(quadroInserir, text="Nome", anchor=W)
lbnome.pack(side="left")
vnome = Entry(quadroInserir)
vnome.pack(side="left", padx=10)

lbfone = Label(quadroInserir, text="Telefone", anchor=W)
lbfone.pack(side="left")
vfone = Entry(quadroInserir)
vfone.pack(side="left", padx=10)

## Butão Inserir
btn_inserir = Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side="left", padx=10)

## LabelFrame, Label, Entry, BUtton => PESQUISAR CONTATOS
quadroPesquisar = LabelFrame(app, text="Pesquisar Contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side="left", padx=10)

btn_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_pesquisar.pack(side="left", padx=10)

btn_todos = Button(quadroPesquisar, text="Todos", command=popular)
btn_todos.pack(side="left", padx=10)











app.mainloop()