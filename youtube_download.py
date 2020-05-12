import pytube
import tkinter
from tkinter import messagebox

def download():
    video_url = str(ed.get())

    try:
        pytube.YouTube(video_url).streams.first().download()
        messagebox.showinfo('Download realizado!','Seu video está na pasta onde se encontra o arquivo!')
    except:
        messagebox.showinfo('Falha do download','Verifique a url do seu video')


# Criação da janela de interação usando kinter

janela = tkinter.Tk()
janela.title("Download de video do Youtube")
janela.geometry('350x110+500+300')

lb = tkinter.Label(janela, text="Cole a URL para realizar o download")
lb.place(x=70, y=5)

ed = tkinter.Entry(janela, width=50)
ed.place(x=20, y=35)

bt = tkinter.Button(janela, width=40, text='Download', command=download)
bt.place(x=27,y=62)

janela.mainloop()
