from tkinter import *
import banco


def gravarDados():
    if tb_nome.get() != "":
        vnome = tb_nome.get()
        vfone = tb_fone.get()
        vmail = tb_mail.get()
        vobs = tb_obs.get("1.0", END)
        vquery=" INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO, T_OBS VALUES  (' "+vnome+", "+vfone+ ", "+vmail+", "+vobs+" '))"
        banco.dml(vquery)
        tb_nome.delete()
        tb_fone.delete()
        tb_email.delete()
        tb_obs.delete("1.0", END)
       
        print("Dados Gravados")
    else:
        print("Error")


    
app = Tk()
app.title("CFB cursos")
app.geometry("500x300")
app.configure(background="#dde")


#anchor=> N=Norte,  S=Sul, E=Leste, W=Oeste
#NE=Nodeste, SE=Sudeste, SO=Sudoeste, No= Noroeste

Label(app, text="Nome", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)

tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#fff", foreground="#009", anchor=W).place(x=10, y=60, width=100, height=20)

tb_fone = Entry(app)
tb_fone.place(x=10, y=80, width=200, height=20)

Label(app, text="Email", background="#fff", foreground="#009", anchor=W).place(x=10, y=110, width=100, height=20)

tb_mail = Entry(app)
tb_mail.place(x=10, y=130, width=200, height=20)

Label(app, text="Obs", background="#fff", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)

tb_obs = Text(app)
tb_obs.place(x=10, y=180, width=300, height=80)

Button(app, text="Imprimir", command=impDados).place(x=10, y=270, width=100, height=20)


app.mainloop()
