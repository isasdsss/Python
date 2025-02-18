from tkinter import*

janela = Tk()
janela.title ('Criando um Label')
janela.geometry('400x350')

#Como criar um label
#Propriedades de um label   font,fg,bg e pady

label_nome = Label(janela, width=20, height=2, text = 'Nome: ', font=('Arial 12 bold'), fg='blue', bg='black') 
label_nome.grid(row=0, column=0,pady=10)


label_idade = Label(janela, width=20, height=2, text = 'Idade: ', font=('Arial 12 bold'),  fg='blue', bg='black')
label_idade.grid(row=1, column=0, pady=10)


label_pais = Label(janela, width=20, height=2, text = 'País: ', font=('Arial 12 bold'),  fg='blue', bg='black')
label_pais.grid(row=2, column=0, pady=10)





janela.mainloop()