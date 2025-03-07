#importando tkinter(Biblioteca de interface gráfica)
from tkinter import *
from tkinter import Tk, ttk
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


janela =Tk()
janela.title("Conversor de moedas")
janela.geometry("300x320")
janela.resizable(width=FALSE, height=FALSE)


#frame da parte de cima
frame_titulo = Frame(janela, width=300, height=60, bg='black', padx=0, pady=0, relief='flat') 
frame_titulo.grid(row=0, column=0, columnspan=2)

#frame da parte de baixo
frame_corpo = Frame(janela, width=300, height=260, bg='white', padx=0, pady=5, relief='flat')
frame_corpo.grid(row=1, column=0, sticky = NSEW)

#Importando Icone
icon = Image.open("icone.png")  
icon = icon.resize((40, 40), Image.LANCZOS)  
icon = ImageTk.PhotoImage(icon)

#label para o titulo
app_nome = Label(frame_titulo, image = icon, compound=LEFT, text='Conversor de Moedas',height=5, pady=30, padx=13, relief='groove', anchor='center', font=('Arial 16 bold'), bg='black', fg='White')
app_nome.place(x=0, y=0)

#label para o resultado
app_resultado = Label(frame_corpo, compound=LEFT, text='10 real',height=2, width= 16, relief='groove', anchor='center', font=('Arial 16 bold'), bg='white', fg='black')
app_resultado.place(x=40, y=10)

#lista de moedas
moeda = ['AOA', 'BRL', 'EUR', 'INR','USD']

#label para os textos e combobox
app_de = Label(frame_corpo, text='De:  ', height=1, width=4, relief='flat', anchor='e', font=('Arial 10 bold'), bg='white', fg='black')
app_de.place(x=40, y=110)  # Ajuste fino na posição

combo_de = Combobox(frame_corpo, width=5, font=('Ivy 12 bold'))
combo_de['values'] = moeda
combo_de.place(x=70, y=110)  # Posicione logo ao lado


#label para os textos e combobox 
app_para = Label(frame_corpo, text='Para:  ', height=1, width=5, relief='flat', anchor='e', font=('Arial 10 bold'), bg='white', fg='black')
app_para.place(x=140, y=110)  # Ajuste fino na posição

combo_para = Combobox(frame_corpo, width=5, font=('Ivy 12 bold'))
combo_para['values'] = moeda
combo_para.place(x=180, y=110)  # Posicione logo ao lado

#Botão resultado
botao_resultado = Button(frame_corpo, compound=LEFT, text='Converter',height=2, width= 10, relief='raised', anchor='center', font=('Arial 16 bold'), bg='white', fg='black')
botao_resultado.place(x=70, y=180)

janela.mainloop()