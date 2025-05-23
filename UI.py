from pathlib import Path
import os
import tkinter as tk
import fD


def getCaminho():
    caminho = entry_caminho.get()
    return caminho

def getUrl():
    url = entry_url.get()
    return url

def download():
    baixar = fD.download(getUrl(), getCaminho())
    if baixar is True:
        entry_url.delete(0, tk.END)
        lb_status.config(text="Baixado com sucesso!")
    else:
        lb_status.config(text="Erro no download")

ui = tk.Tk()
ui.title("Baixador")
ui.geometry("500x500+500+300")
ui.resizable(False, False)

#label e entry do caminho do arquivo
lb_caminho = tk.Label(ui, text="Defina o caminho:")
lb_caminho.place(x=75, y=30)
entry_caminho = tk.Entry(ui, width=50)
entry_caminho.place(x=75, y=50)

#label e entry da url do arquivo
lb_url = tk.Label(ui, text="Qual a url do arquivo a ser baixado?")
lb_url.place(x=75, y=80)
entry_url = tk.Entry(ui, width=50)
entry_url.place(x=75, y=100)

#label de resposta
lb_status = tk.Label(ui, text="")
lb_status.place(x=75, y=150)

#btn download
btn_download = tk.Button(ui, text="Baixar", command=lambda: download(), width=20, height=3)
btn_download.place(x=75,y=200)

ui.mainloop()
