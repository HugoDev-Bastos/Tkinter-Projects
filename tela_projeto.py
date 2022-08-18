from tkinter import *


root = Tk()

root.title("Cadastro de Clientes")
root.configure(background='#655acd')
root.geometry("700x500")
root.resizable(True, True)     
root.maxsize(width=900, height=700)  
root.minsize(width=400, height=300)

#Frames
        
frame_1 = Frame(root, bd = 4, bg='#dfe3ee', highlightbackground='#759fe6',highlightthickness=3)
frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.48 )
        
frame_2 = Frame(root, bd= 4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
frame_2.place(relx=0.02, rely=0.05, relwidth=0.96, relheight=0.48 )
        
# Botões Limpar
bt_limpar = Button(frame_1,text="Limpar")
bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)        
        
# Botões Buscar
bt_buscar = Button(frame_1,text="Buscar")
bt_buscar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

root.mainloop()