from tkinter import *


#Criando a janela
janela = Tk()
janela.geometry('300x180')
janela.config(bg='black')
janela.resizable(width=FALSE, height=FALSE)

#variáveis
global tempo
global rodar
global contador

tempo = '00:00:00'
rodar = False
contador = -5

#Funções


#função para iniciar o cronometro
def iniciar():
    global tempo
    global contador

    if rodar: 
        if contador <= -1:   #loop com condiçao de incremento
            inicio = 'Começando em: ' + str(contador) #converrtendo o contador para string
            label_tempo['text']= inicio
            label_tempo['font']=  'Arial 10'

        else:
             print('ok')
        
        contador +=1

    label_tempo.after(1000,iniciar)


#funçao para iniciar a condiçao
def start():
    global rodar
    rodar = True
    iniciar()

#Criando label
label_app = Label(janela, text='Cronômetro', font='Arial 10', fg='white', bg='black')
label_app.place(x=20, y=5)

label_tempo = Label(janela, text='00:00:00', font='times 50 bold', fg='purple', bg='black')
label_tempo.place(x=20, y=25)

#Botões
botao_iniciar = Button(janela,command=start, text='Iniciar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_iniciar.place(x=20, y=130)


botao_pausar = Button(janela, text='Pausar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_pausar.place(x=105, y=130)


botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_reiniciar.place(x=190, y=130)


janela.mainloop()