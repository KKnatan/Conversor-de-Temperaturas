#convercer de temperatura  com tkinter
from tkinter import *
import tkinter as ttk
#Codigo



tela= Tk()
tela.title('Conversor de temperaturas')
tela.geometry('430x340')
tela.minsize(430,340)
tela.maxsize(430,340)
fare=StringVar()
kelvin1=StringVar()
tela.configure(background='#353430')

#codigo
def fahrenheit():
    user=celcius_entry.get()
    f= 9* int(user)/5+32
    fare.set(f)
        
def kelvin():
    user=celcius_entry.get()
    k= int(user)+273
    kelvin1.set(k)

#Configuração da grade(grid)
tela.columnconfigure(0, weight=7)
tela.columnconfigure(1, weight=7)

#Celcius texto
celcius_label= ttk.Label(tela,
                        text='Conversor\n de\n temperatura',
                        fg='White', bg='#353430',
                        font=('Arial', 20,'bold',))
celcius_label.grid(column=0,
                   row=0,
                   sticky=N,
                   padx=110)
#Digitar temperatura texto
temp_label=ttk.Label(tela,
                    text='Digite uma temperatura em celcius(°c)',
                    fg='White',
                    bg='#353430',
                    font=('Arial', 13,'bold'))
temp_label.grid(column=0,
                row=1)

#lugar onde vai colocar a temperatura
celcius_entry=ttk.Entry(tela,width=20,font=60,justify=CENTER)
celcius_entry.grid(column=0,row=2,)

#Qual unidade de temperatura
unidae_temp=ttk.Label(tela,
                      text='transformar em:',
                      font=('Arial',15,'bold'),
                      fg='Black',
                      bg='White',
                      relief=SOLID
)
unidae_temp.grid(column=0,
                 row=3,
                 padx=(0,250),
                 pady=(20,0))

#Kelvin

kelvin_botao=ttk.Button(tela,text='Kelvin',relief=RAISED,font=2,command=kelvin)
kelvin_botao.grid(
                column=0,
                row=4,
                pady=(10,0),
                padx=(0,330)
)
Kelvin_texto=ttk.Entry(tela,
                       width=20,
                        font=60,
                        justify=CENTER,
                        textvariable=kelvin1
)          

Kelvin_texto.grid(column=0,row=4,padx=(0,30),pady=(10,0))

kelvin_lado= ttk.Label(tela,text='K', font=0.3,relief=RAISED,background='White',fg='Black')
kelvin_lado.grid(column=0,row=4,padx=(185,0),pady=(10,0))

#Fahrenheit texto 
fahrenheit_botao=ttk.Button(tela,text='Fahrenheit', relief=RAISED,font=2,command=fahrenheit)
fahrenheit_botao.grid(
                column=0,
                row=5,
                pady=(15,0),
                padx=(0,330)
)
fahrenheit_texto=ttk.Entry(tela,width=20,font=60,justify=CENTER, textvariable=fare)

fahrenheit_texto.grid(column=0,
                  row=5,
                  padx=(0,30),
                  pady=(10,0))
fahrenheit_botaolado=ttk.Label(tela,text='°F', font=0.3,relief=RAISED,background='White',fg='Black')
fahrenheit_botaolado.grid(column=0,row=5,padx=(185,0),pady=(10,0))
tela.mainloop()
