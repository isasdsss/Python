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
frame= frame_tela.grid(row=0, column=0)

frame_corpo= Frame(janela, width=235, height=268)
frame= frame_corpo.grid(row=1, column=0)

#LABEL
app_label= Label(frame_tela, text="12345678", width=16, height=2, padx=7, relief=FLAT, anchor="e", justify="right", font=('Ivy 18 bold'), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)

#botões
b_1 = Button(frame_corpo, text="C",width=11, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao de limpar/clean
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #modulo
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #divisao
b_3.place(x=177, y=0)


b_4 = Button(frame_corpo, text="7",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_5.place(x=60, y=52)
b_6 = Button(frame_corpo, text="9",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, text="*",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_7.place(x=177, y=52)


b_8 = Button(frame_corpo, text="4",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text="5",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_9.place(x=60, y=104)
b_10 = Button(frame_corpo, text="6",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, text="-",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_11.place(x=177, y=104)



b_12 = Button(frame_corpo, text="1",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, text="2",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_13.place(x=60, y=156)
b_14 = Button(frame_corpo, text="3",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, text="+",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, text="0",width=11, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botao de limpar/clean
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".",width=5, height=2, bg=cor4, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #modulo
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, text="=",width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #divisao
b_18.place(x=177, y=208)



janela.mainloop()