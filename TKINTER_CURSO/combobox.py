from tkinter.ttk import *  # Importação correta
from tkinter import *


janela = Tk()  #criação da janela
janela.title('Combobox') #titulo da janela
janela.geometry('400x300')

#Funçao para mostrar valor feito

def obter():
    resultado = combo.get()
    label_resultado.config(text=f'Sua escolha: {resultado}')  # Atualiza o Label

label_pais = Label(janela, text='Defina o melhor país: ', width=20, height=2, font='Arial 10 bold' )
label_pais.grid(row=0, column=0, pady=10, padx=10 )

# Label para mostrar o resultado
label_resultado = Label(janela, text='', width=30, height=2, font='Arial 10 bold')
label_resultado.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

#Combobox
combo = Combobox(janela)
combo['values'] = ('Brasil', 'Portugal')
combo.current(0)
combo.grid(row=0, column=1, pady=10, padx=10)  # Adiciona a Combobox à janela

botao = Button(janela, width=20, command=obter, height=2, text='Sua escolha', relief='groove')
botao.grid(row=1, column=0, pady=10, padx=10)


janela.mainloop()