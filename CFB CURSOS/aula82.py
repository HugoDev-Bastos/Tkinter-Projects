from ast import Delete
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import left
import banco

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nomes order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("","end", values=i)

def inserir():
    if vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="Error", message="Digite todos os dados!")
        return
    try:
        vquery="INSERT INTO tb_nomes (nome, fone) VALUES ("+vnome.get()+","+vfone.get()+")"
        banco.dml(vquery)
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
        vquery = " DELETE FROM tb_nomes WHERE id="+vid
        banco.dml(vquery)
    except:
        messagebox.showinfo(title="Error", message="Erro ao deletar")
        return
    tv.delete(itemSelecionado)


def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_nome WHERE nome LIKE '%" + vnomepesquisar.get()+ "%'"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)    
    
app = Tk()
app.title("")


## TrenView
quadroGrid = LabelFrame(app, text="Contatos")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns=("id", "nome", "telefone"), show="headings")
tv.column("id", minwidth=0, width=50)
tv.column("nome", minwidth=0, width=250)
tv.column("telefone", minwidth=0, width=100)
tv.heading("id", text="ID")
tv.heading("nome", text="Nome")
tv.heading("telefone", text="Telefone")
tv.pack()
popular()

## Label e Campos de Entrada
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

## Butão Pesquisar
quadroPesquisar = LabelFrame(app, text="Inserir Novos Contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

btn_consultar = Button(quadroPesquisar, text="Consultar", command=pesquisar)
btn_consultar.pack(side="left", padx=10)


## Butão Deletar
btn_deletar = Button(quadroInserir, text="Deletar", command=deletar)
btn_deletar.pack(side="left", padx=10)





app.mainloop()