from tkinter import *
import os

app = Tk()
app.title("CFB cursos")
app.geometry("500x300")
app.configure(background="#dde")

c=os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"

def impDados():
    arquivo=open(nomeArquivo,"a")
    arquivo.write("Nome....: %s" % vnome.get())
    arquivo.write("\nTelefone....: %s" % vfone.get())
    arquivo.write("\nE-mail....: %s" % vmail.get())
    arquivo.write("\nObs....: %s" % vobs.get("1.0", END))
    arquivo.write("\n\n")
    arquivo.close()


#anchor=> N=Norte,  S=Sul, E=Leste, W=Oeste
#NE=Nodeste, SE=Sudeste, SO=Sudoeste, No= Noroeste

Label(app, text="Nome", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)

vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#fff", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)

vfone = Entry(app)
vfone.place(x=10, y=80, width=200, height=20)

Label(app, text="Email", background="#fff", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)

vmail = Entry(app)
vmail.place(x=10, y=130, width=200, height=20)

Label(app, text="Obs", background="#fff", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)

vobs = Text(app)
vobs.place(x=10, y=180, width=300, height=80)

Button(app, text="Imprimir", command=impDados).place(x=10, y=270, width=100, height=20)


app.mainloop()
