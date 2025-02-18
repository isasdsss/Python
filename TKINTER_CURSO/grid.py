from tkinter import*

janela = Tk()
janela.title ('Criando um Label')
janela.geometry('400x350')


label_nome = Label(janela, width=20, height=2, text = 'Nome: ', font=('Arial 12 bold'), fg='white', bg='blue') 
label_nome.place(x=50, y=10)
nome = Label(janela, width=20, height=2, text = 'João', font=('Arial 12 bold'), fg='white', bg='blue') 
nome.place(x=300, y=10)

label_idade = Label(janela, width=20, height=2, text = 'Idade: ', font=('Arial 12 bold'),  fg='white', bg='blue')
label_idade.place(x=50, y=60)
idade = Label(janela, width=20, height=2, text = '17 anos', font=('Arial 12 bold'), fg='white', bg='blue') 
idade.place(x=300, y=60)




label_pais = Label(janela, width=20, height=2, text = 'País: ', font=('Arial 12 bold'),  fg='white', bg='blue')
label_pais.place(x=50, y =110)
pais= Label(janela, width=20, height=2, text = 'Brasil', font=('Arial 12 bold'), fg='white', bg='blue') 
pais.place(x=300, y=110)

janela.mainloop()