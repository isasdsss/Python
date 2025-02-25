from tkinter.ttk import *  # Importação correta
from tkinter import*

janela = Tk()
janela.title('RadioButton') #titulo da janela
janela.geometry('400x300')   


#Funçao para obter escolha

def mostrar_escolha():
    resultado = escolha.get()
    label_resultado.config(text=f'Sua escolha: {resultado}')  # Atualiza o Label

#Variavel para armazenar o valor
escolha = IntVar()

#Criando as escolhas 
radio_01 = Radiobutton(janela, text='Primeiro', value=1, variable=escolha, command=mostrar_escolha )  #Value serve para definir o tipo da variavel
radio_01.grid(row=0, column=0)

radio_02= Radiobutton(janela, text='Segundo', value=2, variable=escolha, command=mostrar_escolha )
radio_02.grid(row=1, column=0)


# Label para mostrar o resultado
label_resultado = Label(janela, text='', width=30, height=2, font='Arial 10 bold')
label_resultado.grid(row=3, column=0, columnspan=2, pady=10, padx=10)


janela.mainloop()