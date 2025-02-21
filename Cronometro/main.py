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
global limitador

tempo = '00:00:00'
rodar = False
contador = -5
limitador = 59

#Funções


#função para iniciar o cronometro
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar: 
        #antes do cronometro comecar
        if contador <= -1:   #loop com condiçao de incremento
            inicio = 'Começando em: ' + str(contador) #converrtendo o contador para string
            label_tempo['text']= inicio
            label_tempo['font']=  'Arial 10'

      
        # Rodando o cronômetro
        else:
            label_tempo.config(font='Times 50 bold')

            h, m, s = map(int, tempo.split(':'))  # Convertendo tempo para inteiros
            s = contador  # Atualizando segundos corretamente

            if s >= limitador:  # Quando os segundos atingem o limite
                contador = 0
                m += 1  # Incrementa os minutos
                

            # Garantindo que sempre haja dois dígitos em cada campo de tempo
            temporario = f"{h:02}:{m:02}:{s:02}"
            label_tempo.config(text=temporario)  # Atualizando a interface gráfica
            tempo = temporario

        label_tempo.after(1000, iniciar)  # Chamando a função novamente após 1 segundo
        contador += 1

#funçao para iniciar 
def start():
    global rodar
    rodar = True
    iniciar()

#funçao para iniciar 
def pausar():
    global rodar
    rodar = False
   
#funçao para reiniciar
def reiniciar():
    global rodar, contador
    rodar = False
    contador = 0
    label_tempo['text'] = '00:00:00'


#Criando label
label_app = Label(janela, text='Cronômetro', font='Arial 10', fg='white', bg='black')
label_app.place(x=20, y=5)

label_tempo = Label(janela, text='00:00:00', font='times 50 bold', fg='purple', bg='black')
label_tempo.place(x=20, y=25)

#Botões
botao_iniciar = Button(janela,command=start, text='Iniciar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_iniciar.place(x=20, y=130)


botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_pausar.place(x=105, y=130)


botao_reiniciar = Button(janela, text='Reiniciar', command=reiniciar, width=10, height=2,font='Arial 10', relief='raised', overrelief='ridge', bg='black', fg='white')
botao_reiniciar.place(x=190, y=130)


janela.mainloop()