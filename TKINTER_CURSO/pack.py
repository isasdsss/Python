from tkinter import*

janela = Tk()
janela.title ('Criando um Label')
janela.geometry('400x350')


label_nome = Label(janela, width=20, height=2, text = 'Nome: ', font=('Arial 12 bold'), fg='white', bg='blue') 
label_nome.pack(side=LEFT)

nome = Label(janela, width=20, height=2, text = 'João', font=('Arial 12 bold'), fg='white', bg='blue') 
nome.pack(side=LEFT)


label_idade = Label(janela, width=20, height=2, text = 'Idade: ', font=('Arial 12 bold'),  fg='white', bg='blue')
label_idade.pack(side=LEFT)

idade = Label(janela, width=20, height=2, text = '17 anos', font=('Arial 12 bold'), fg='white', bg='blue') 
idade.pack(side=LEFT)




label_pais = Label(janela, width=20, height=2, text = 'País: ', font=('Arial 12 bold'),  fg='white', bg='blue')
label_pais.pack(side=LEFT)

pais= Label(janela, width=20, height=2, text = 'Brasil', font=('Arial 12 bold'), fg='white', bg='blue') 
pais.pack(side=LEFT)

janela.mainloop()