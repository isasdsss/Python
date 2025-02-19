from tkinter import *


#Criando a janela
janela = Tk()
janela.geometry('300x180')
janela.config(bg='black')
janela.resizable(width=FALSE, height=FALSE)


#Criando label
label_app = Label(janela, text='Cronômetro', font='Arial 10', fg='white', bg='black')
label_app.place(x=20, y=5)

label_app = Label(janela, text='00:00:00', font='times 50 bold', fg='purple', bg='black')
label_app.place(x=20, y=25)

#Botões
botao_iniciar = Button(janela, text='Iniciar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_iniciar.place(x=20, y=130)


botao_pausar = Button(janela, text='Pausar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_pausar.place(x=105, y=130)


botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_reiniciar.place(x=190, y=130)


janela.mainloop()