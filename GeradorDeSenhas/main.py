from tkinter.ttk import *  # Importação correta
from tkinter import*
from PIL import Image, ImageTk
import string
import random


janela = Tk()
janela.title('Gerador De Senhas')
janela.geometry('305x360')
janela.configure(bg='White')


#Frame da parte de cima
frame_cima = Frame(janela, width=295, height=50, pady=0, padx=0, relief='flat')
frame_cima.grid(row= 0, column=0, sticky=NSEW)

img = Image.open('logo.png')
img = img.resize((30, 40), Image.LANCZOS)  # Use LANCZOS se a versão for recente
image = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=image, compound='left', padx=10, relief='flat', anchor='nw', bg='white')
app_logo.place(x=1, y=0)

app_nome = Label(frame_cima, text='Gerador De Senhas', width=20, height=2, font='Ivy 16 bold', padx=10, relief='flat', bg='white')
app_nome.place(x=35, y=0)

app_linha = Label(frame_cima, width=295, height=2, font='Ivy 16 bold', bg='orange', relief='flat')  
app_linha.place(x=0, y=45)


frame_baixo = Frame(janela, width=295, height=310, pady=0, padx=0, relief='flat', bg='white')
frame_baixo.grid(row= 1, column=0, sticky=NSEW)

app_senha = Label(frame_baixo, text=' - - - - ', width=21, height=2, font='Ivy 12 bold', fg='black', relief='groove', anchor = 'center',  bg='white')  
app_senha.grid(row= 0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)


app_info = Label(frame_baixo, text='Número total de caracteres na senha', height=2, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white')  
app_info.grid(row= 1, column=0, columnspan=1, sticky=NSEW, padx=3, pady=0)

Var = IntVar()
Var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=Var)  #define o intervalo de 0 a 20
spin.grid(row=1, column=0, sticky=NW, padx=5, pady=30)

#Variavel das letras
alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '(){}[]*;:/_-'


#Frame dos caracteres
frame_caracteres = Frame(frame_baixo,width=295, height=210, relief='flat', padx=0, pady=0,  bg='white' )  
frame_caracteres.grid(row= 3, column=0, columnspan=3, sticky=NSEW)


#primeiro checkbox
estado_1 = StringVar()
estado_1.set(False)
estado_1 = Checkbutton(frame_caracteres, width=2, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat',  bg='white')
estado_1.grid(row=0, column=1, sticky=NSEW, padx=5)


app_info = Label(frame_caracteres, text='ABC letras maiúsculas', height=1, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white', padx=0)  
app_info.grid(row= 0, column=2, columnspan=1, sticky=NW, padx=2, pady=5)


#2 checkbox
estado_2 = StringVar()
estado_2.set(False)
estado_2 = Checkbutton(frame_caracteres, width=2, var=estado_2, onvalue=alfabeto_menor, offvalue='off', relief='flat',  bg='white')
estado_2.grid(row=1, column=1, sticky=NSEW, padx=5)


app_info = Label(frame_caracteres, text='ABC letras minúsculas', height=1, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white', padx=0)  
app_info.grid(row=1, column=2, columnspan=1, sticky=NW, padx=2, pady=5)



#3 checkbox
estado_3 = StringVar()
estado_3.set(False)
estado_3 = Checkbutton(frame_caracteres, width=2, var=estado_3, onvalue=numeros, offvalue='off', relief='flat',  bg='white')
estado_3.grid(row=2, column=1, sticky=NSEW, padx=5)

app_info = Label(frame_caracteres, text='Números', height=1, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white', padx=0)  
app_info.grid(row=2, column=2, columnspan=1, sticky=NW, padx=2, pady=5)


#4 checkbox
estado_4 = StringVar()
estado_4.set(False)
estado_4 = Checkbutton(frame_caracteres, width=2, var=estado_4, onvalue=numeros, offvalue='off', relief='flat',  bg='white')
estado_4.grid(row=3, column=1, sticky=NSEW, padx=5)

app_info = Label(frame_caracteres, text='Símbolos', height=1, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white', padx=0)  
app_info.grid(row=3, column=2, columnspan=1, sticky=NW, padx=2, pady=5)

#Botões

botao_gerar_senha= Button(frame_caracteres, text='Gerar Senha', font='Ivy 10 bold ', width=35, relief='groove', anchor = 'center',  bg='orange', fg='black')
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW , padx=7, pady=10, columnspan=5 )


botao_copiar= Button(frame_baixo, text='copiar', font='Ivy 10 bold ',width=5, height=1, relief='groove', anchor = 'center',  bg='white', fg='black')
botao_copiar.grid(row=0, column=1, sticky=NSEW , padx=5, pady=7, columnspan=1 )




janela.mainloop()