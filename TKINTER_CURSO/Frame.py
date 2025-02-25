from tkinter import*

janela = Tk()
janela.title('Frame') #titulo da janela
janela.geometry('400x300') 


#Bandeira do chile
frame_branca = Frame(janela, width=400, height=150, bg='white')
frame_branca.place(x=0,y=0)

frame_vermelho = Frame(janela, width=400, height=150, bg='red')
frame_vermelho.place(x=0,y=150)


frame_azul = Frame(frame_branca, width=135, height=150, bg='blue')
frame_azul.place(x=0,y=0)


janela.mainloop()