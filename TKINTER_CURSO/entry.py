from tkinter import*

janela = Tk()
janela.title ('Caixa de Entrada')
janela.geometry('450x300')


#Funções

def Obter():

    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_res['text'] = nome
    label_idade_res['text'] = idade
    label_pais_res['text'] = pais

    nome = entry_nome.delete(0,END)
    idade = entry_idade.delete(0,END)
    pais = entry_pais.delete(0,END)




#nome
label_nome = Label(janela, width=8, height=2, text='Nome:', font=('Arial 10'), anchor='w')
label_nome.grid(row= 0, column=0, padx=10, pady=5, sticky=NSEW)

entry_nome = Entry(janela, width=10, font=('arial 10'))
entry_nome.grid(row= 0, column=1, padx=10, pady=5)

#nome respostas
label_nome_res = Label(janela, width=8, height=2, text='', font=('Arial 10'))
label_nome_res.grid(row= 0, column=2, padx=10, pady=5, sticky=NSEW)


#idade
label_idade = Label(janela, width=8, height=2, text='Idade:', font=('Arial 10'), anchor='w')
label_idade.grid(row= 1, column=0, padx=10, pady=5, sticky=NSEW)


entry_idade = Entry(janela, width=10, font=('arial 10'))
entry_idade.grid(row= 1, column=1, padx=10, pady=5)

#idade resposta
label_idade_res = Label(janela, width=8, height=2, text='', font=('Arial 10'))
label_idade_res.grid(row= 1, column=2, padx=10, pady=5, sticky=NSEW)

#pais
label_pais = Label(janela, width=8, height=2, text='País:', font=('Arial 10'), anchor='w')
label_pais.grid(row= 2, column=0, padx=10, pady=5, sticky=NSEW)

entry_pais = Entry(janela, width=10, font=('arial 10'))
entry_pais.grid(row= 2, column=1, padx=10, pady=5)

#pais resposta
label_pais_res = Label(janela, width=8, height=2, text='', font=('Arial 10'))
label_pais_res.grid(row= 2, column=2, padx=10, pady=5, sticky=NSEW)

botao = Button(janela,command=Obter, width=20, height=2, text='Mostrar Dados', relief='groove', fg='purple')
botao.grid(row=3, column=1, padx=5, pady=10)

janela.mainloop()