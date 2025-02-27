from tkinter.ttk import *  # Importação correta
from tkinter import*
from PIL import Image, ImageTk


janela = Tk()
janela.title('Gerador De Senhas')
janela.geometry('295x350')
janela.configure(bg='White')


#Frame da parte de cima
frame_cima = Frame(janela, width=295, height=50, pady=0, padx=0, relief='flat')
frame_cima.grid(row= 0, column=0, sticky=NSEW)

img = Image.open('logo.png')
img = img.resize((30, 40), Image.LANCZOS)  # Use LANCZOS se a versão for recente
image = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=image, compound='left', padx=10, relief='flat', anchor='nw', bg='white')
app_logo.place(x=1, y=0)

app_nome = Label(frame_cima, text='Gerador De Senhas', width=20, height=2, font='Ivy 16 bold', padx=10, relief='flat', bg='white')
app_nome.place(x=35, y=0)

app_linha = Label(frame_cima, width=295, height=2, font='Ivy 16 bold', bg='orange', relief='flat')  
app_linha.place(x=0, y=45)


frame_baixo = Frame(janela, width=295, height=310, pady=0, padx=0, relief='flat')
frame_baixo.grid(row= 1, column=0, sticky=NSEW)

janela.mainloop()