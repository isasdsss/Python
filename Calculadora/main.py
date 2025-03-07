#importando tkinter(Biblioteca de interface gráfica)
from tkinter import *
from tkinter import ttk


#Definindo as cores que vou usar

cor1= "#2d1169" #roxoescuro
cor2= "#ffffff" #branco
cor3= "#5d1499" #roxoclaro
cor4= "#dfbaf7" #lilás
cor5= "#fffa66" #amarelo



janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor2)




#frames
frame_tela= Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variável todos os valores

todos_valores = ""  # inicia uma string vazia para armazenar os valores digitados pelo usuário ao longo do uso da calculadora.

#funçao : Essa função é responsável por armazenar e exibir os valores digitados conforme o usuário interage com a interface.
def entrar_valores(event):
    
    global todos_valores #será modificada dentro da função. Isso permite que seu valor seja atualizado e mantido a cada entrada do usuário.

    todos_valores += str(event)

    #passando o valor para a tela
    valor_texto.set(todos_valores)


#Função para calcular
def calcular():
    global todos_valores     # A variável 'todos_valores' é global e acessada dentro da função
    resultado= eval(todos_valores)   # A função 'eval()' avalia o conteúdo de 'todos_valores' como uma expressão Python e armazena o resultado
    print(resultado)    

    valor_texto.set(str(resultado))        # Atualiza a variável 'valor_texto' com o resultado calculado, transformando-o em string
    # A mudança no 'valor_texto' faz o 'Label' que está associado a ele ser atualizado automaticamente


    #Função limpar tela
def limpar_tela():
    global todos_valores  # Acessa a variável global 'todos_valores'
    todos_valores = ""    # Limpa os valores armazenados para o próximo cálculo
    valor_texto.set("")   # Limpa o conteúdo exibido na tela
        


#LABEL

# Criação de um objeto 'StringVar' que irá armazenar o valor do texto para o 'Label'
valor_texto = StringVar()


# Criação de um 'Label' com a variável 'valor_texto' como conteúdo de texto
app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=2, padx=7, relief=FLAT, anchor="e", justify="right", font=('Ivy 18 bold'), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)

#botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C",width=11, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao de limpar/clean
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #modulo
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'),text="/",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #divisao
b_3.place(x=177, y=0)


b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'),text="7",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'),text="8",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'),text="9",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'),text="*",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_7.place(x=177, y=52)


b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'),text="4",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'),text="5",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'),text="6",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'),text="-",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_11.place(x=177, y=104)



b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'),text="1",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'),text="2",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'),text="3",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'),text="+",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'),text="0",width=11, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao de limpar/clean
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'),text=".",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #modulo
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command=calcular, text="=",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #divisao
b_18.place(x=177, y=208)




janela.mainloop()