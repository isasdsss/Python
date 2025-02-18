from tkinter import*

janela = Tk()
janela.title ('Criando um Label')
janela.geometry('450x300')

contador = 0

def  executar():

    global contador

    texto1 = 'Número ímpar: '
    texto2 = 'Número par: '

    if (contador %2) == 0:
        resultado = texto2 + str(contador)
        label['text'] = resultado
    else:
      resultado = texto1 + str(contador)
      label['text'] = resultado
      
    contador +=1


label = Label(janela, width=30, height=2, text='Vereficando Números (par/ímpar) ', relief='flat', fg='purple', bg='black', font=('arial',10))
label.grid(row=0, column=0, padx=5, pady=10)

botao = Button(janela,command=executar, width=20, height=2, text='Clique aqui!', relief='groove', fg='purple')
botao.grid(row=0, column=1, padx=5, pady=10)
janela.mainloop()