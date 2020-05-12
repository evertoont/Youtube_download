import pytube
import tkinter
from tkinter import messagebox


# Criação da janela de interação usando kinter

janela = tkinter.Tk()
janela.title("Download de video do Youtube")
janela.geometry('350x110+500+300')

lb = tkinter.Label(janela, text="Cole a URL para realizar o download")
lb.place(x=70, y=5)

ed = tkinter.Entry(janela, width=50)
ed.place(x=20, y=35)

janela.mainloop()
