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
b_confirmar = Button(frame_baixo,text='Enviar', width=40, height=2, bg='purple', fg='white', font='Ivy 8 bold', relief='raised', overrelief='ridge')
b_confirmar.place(x=10, y=180)

janela.mainloop()