from tkinter.ttk import *  # Importação correta
from tkinter import*
from tkinter import messagebox

janela = Tk()
janela.title('Login')
janela.geometry('310x300')
janela.resizable(FALSE,FALSE)
janela.configure(bg='White')

#Frames

frame_cima = Frame(janela, width=310, height=50, bg='white', relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW )

frame_baixo = Frame(janela, width=310, height=250, bg='white', relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW )


#Funções

credencial = ['Isabela', '123456789']
# funçao verificar senha
def verificar_senha():
    nome = e_nome.get()
    senha = e_senha.get()

    if nome == 'admin' and senha =='admin':
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    elif credencial[0] == nome and credencial[1] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")

        #apaga o frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    else:
        
        messagebox.showerror("Erro", "Nome ou senha incorretos!")

#funçao apos vereficar
def nova_janela():

    l_login = Label(frame_cima, text='Usuário: ' + credencial[0], anchor=NE, font=('Ivy 12'), fg='black', bg='white')
    l_login.place(x=5, y=5)

    l_linha = Label(frame_cima, width=275, anchor=NW, font=('Ivy 1 bold'), bg='purple')
    l_linha.place(x=10, y=46)

    l_login = Label(frame_baixo, text='Seja Bem-vindo(a): ' + credencial[0], anchor=NE, font=('Ivy 12'), fg='black', bg='white')
    l_login.place(x=5, y=5)



#Configurando Frame_Cima (label)

l_login = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), fg='black', bg='white')
l_login.place(x=5, y=5)


l_linha = Label(frame_cima, width=275, anchor=NW, font=('Ivy 1 bold'), bg='purple')
l_linha.place(x=10, y=46)

#Configurando frame_baixo(label)

# NOME LABEL
l_nome = Label(frame_baixo, text='Nome *', anchor=NE, font=('Ivy 10'), fg='black', bg='white')
l_nome.place(x=15, y=25)

#Entry nome
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), relief='solid', highlightthickness=1,  fg='black', bg='white')
e_nome.place(x=14, y=50)

# SENHA LABEL
l_senha = Label(frame_baixo, text='Senha *', anchor=NE, font=('Ivy 10'), fg='black', bg='white')
l_senha.place(x=15, y=100)

#Entry nome
e_senha = Entry(frame_baixo, width=25, justify='left', show='*', font=('', 15), relief='solid', highlightthickness=1,  fg='black', bg='white')
e_senha.place(x=14, y=125)

#Botão
b_confirmar = Button(frame_baixo,command=verificar_senha, text='Enviar', width=40, height=2, bg='purple', fg='white', font='Ivy 8 bold', relief='raised', overrelief='ridge')
b_confirmar.place(x=10, y=180)


janela.mainloop()