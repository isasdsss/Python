#importando tkinter(Biblioteca de interface gráfica)
from tkinter import *
from tkinter import Tk, ttk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import requests
import json
import  string


janela =Tk()
janela.title("Conversor de moedas")
janela.geometry("300x320")
janela.resizable(width=FALSE, height=FALSE)

#---------Divisão dos frames 

#frame da parte de cima
frame_titulo = Frame(janela, width=300, height=60, bg='black', padx=0, pady=0, relief='flat') 
frame_titulo.grid(row=0, column=0, columnspan=2)

#frame da parte de baixo
frame_corpo = Frame(janela, width=300, height=260, bg='white', padx=0, pady=5, relief='flat')
frame_corpo.grid(row=1, column=0, sticky = NSEW)

#Criando Função
def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrado = app_conversao.get()

    response = requests.get(f'https://v6.exchangerate-api.com/v6/660c6295eb4c6f07b59cfe4f/latest/{moeda_de}')
    dados = response.json()  # Usa .json() em vez de json.loads()
    cambio = dados['conversion_rates'][moeda_para]



    resultado = float(valor_entrado) * float(cambio)

    if moeda_para == 'USD': 
        simbolo = '$'
    elif moeda_para == 'EUR': 
        simbolo = '€'
    elif moeda_para == 'INR': 
        simbolo = '₹'
    elif moeda_para == 'AOA': 
        simbolo = 'Kz'
    else:
        simbolo = 'R$'

    moeda_equivalente = simbolo + '{:,.2f}'.format(resultado)
    app_resultado['text'] = moeda_equivalente

#Importando Icone
icon = Image.open("icone.png")  
icon = icon.resize((40, 40), Image.LANCZOS)  
icon = ImageTk.PhotoImage(icon)

#label para o titulo
app_nome = Label(frame_titulo, image = icon, compound=LEFT, text='Conversor de Moedas',height=5, pady=30, padx=13, relief='groove', anchor='center', font=('Arial 16 bold'), bg='black', fg='White')
app_nome.place(x=0, y=0)

#label para o resultado
app_resultado = Label(frame_corpo, compound=LEFT, text='',height=2, width= 16, relief='solid', anchor='center', font=('Arial 16 bold'), bg='white', fg='black')
app_resultado.place(x=40, y=10)

#lista de moedas
moeda = ['AOA', 'BRL', 'EUR', 'INR','USD']

#label para os textos e combobox
app_de = Label(frame_corpo, text='De: ', height=1, width=4, relief='flat', anchor='e', font=('Arial 10 bold'), bg='white', fg='black')
app_de.place(x=40, y=90)  # Ajuste fino na posição

combo_de = Combobox(frame_corpo, width=5, font=('Ivy 12 bold'))
combo_de['values'] = moeda
combo_de.place(x=40, y=110)  # Posicione logo ao lado


#label para os textos e combobox 
app_para = Label(frame_corpo, text='Para: ', height=1, width=5, relief='flat', anchor='e', font=('Arial 10 bold'), bg='white', fg='black')
app_para.place(x=180, y=90)  # Ajuste fino na posição

combo_para = Combobox(frame_corpo, width=5, font=('Ivy 12 bold'))
combo_para['values'] = moeda
combo_para.place(x=180, y=110)  # Posicione logo ao lado

#Entry para a conversão
app_conversao = Entry(frame_corpo, width= 18, relief='solid', justify='center',font=('Arial 16 bold'), bg='white', fg='black')
app_conversao.place(x=40, y=150)


#Botão resultado
botao_resultado = Button(frame_corpo,command=converter, compound=LEFT, text='Converter',height=1, width= 16, relief='raised', anchor='center',overrelief='ridge', font=('Arial 16 bold'), bg='white', fg='black')
botao_resultado.place(x=40, y=200)

janela.mainloop()