from tkinter import *

cor1= ''

janela = Tk()  #criação da janela
janela.title('Criando uma janela') #titulo da janela
janela.geometry('600x250') #como definir o tamanho de uma janela
janela.config(bg='blue')#alterando a cor de fundo


janela.resizable(width=False, height=True) #janela nao redimensionavel

janela.mainloop()


