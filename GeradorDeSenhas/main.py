from tkinter.ttk import *  # Importação correta
from tkinter import*
from tkinter import messagebox
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



#-------------------Funçoes-----------------------

#Variavel das letras

def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '(){}[]*;:/_-'

    combinar = ""

    if estado_1.get() == "on":
        combinar += alfabeto_maior
    
    if estado_2.get() == "on":
        combinar += alfabeto_menor

    if estado_3.get() == "on":
        combinar += numeros

    if estado_4.get() == "on":
        combinar += simbolos

    # Verifica se algum caractere foi selecionado
    if not combinar:
        app_senha['text'] = "Selecione pelo menos um tipo"
        return

    comprimento = int(spin.get())

    # Gera a senha aleatória
    senha = "".join(random.sample(combinar, comprimento))
    app_senha['text'] = senha


    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")

    botao_copiar= Button(frame_baixo, command=copiar_senha, text='copiar', font='Ivy 10 bold ',width=5, height=1, relief='groove', anchor = 'center',  bg='white', fg='black')
    botao_copiar.grid(row=0, column=1, sticky=NSEW , padx=5, pady=7, columnspan=1 )




frame_baixo = Frame(janela, width=295, height=310, pady=0, padx=0, relief='flat', bg='white')
frame_baixo.grid(row= 1, column=0, sticky=NSEW)

app_senha = Label(frame_baixo, text=' - - - - ', width=21, height=2, font='Ivy 12 bold', fg='black', relief='groove', anchor = 'center',  bg='white')  
app_senha.grid(row= 0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)


app_info = Label(frame_baixo, text='Número total de caracteres na senha', height=2, font='Ivy 10 bold ', fg='black', relief='flat', anchor = 'nw',  bg='white')  
app_info.grid(row= 1, column=0, columnspan=1, sticky=NSEW, padx=3, pady=0)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)  #define o intervalo de 0 a 20
spin.grid(row=1, column=0, sticky=NW, padx=5, pady=30)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '(){}[]*;:/_-'

#Frame dos caracteres
frame_caracteres = Frame(frame_baixo, width=295, height=210, relief='flat', padx=0, pady=0,  bg='white' )  
frame_caracteres.grid(row= 3, column=0, columnspan=3, sticky=NSEW)

# Criar variáveis de controle para os checkboxes
# Criar variáveis de controle para os checkboxes com valor inicial "off"
estado_1 = StringVar(value="off")
estado_2 = StringVar(value="off")
estado_3 = StringVar(value="off")
estado_4 = StringVar(value="off")


# Corrigir os checkbuttons, mantendo a StringVar
Checkbutton(frame_caracteres, text="Maiúsculas", variable=estado_1, onvalue="on", offvalue="off", relief='flat', bg='white').grid(row=0, column=1, sticky=W, padx=5)
Checkbutton(frame_caracteres, text="Minúsculas", variable=estado_2, onvalue="on", offvalue="off", relief='flat', bg='white').grid(row=1, column=1, sticky=W, padx=5)
Checkbutton(frame_caracteres, text="Números", variable=estado_3, onvalue="on", offvalue="off", relief='flat', bg='white').grid(row=2, column=1, sticky=W, padx=5)
Checkbutton(frame_caracteres, text="Símbolos", variable=estado_4, onvalue="on", offvalue="off", relief='flat', bg='white').grid(row=3, column=1, sticky=W, padx=5)

app_info = Label(frame_caracteres,  height=1, fg='black', relief='flat', anchor = 'nw',  bg='white', padx=0)  
app_info.grid(row=3, column=2, columnspan=1, sticky=NW, padx=2, pady=5)

#Botões

botao_gerar_senha= Button(frame_caracteres, command=criar_senha, text='Gerar Senha', font='Ivy 10 bold ', width=35, relief='groove', anchor = 'center',  bg='orange', fg='black')
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW , padx=7, pady=10, columnspan=5 )






janela.mainloop()