import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
from tkinter import filedialog
import urllib.request
from PIL import Image
import webbrowser

def nome(a):
    global titulo
    titulo = entrada.get()
    print(f"{titulo}")
    entrada.delete(0, tk.END)
    return a


def peso(b):
    global peso
    peso = float (entrada2.get())
    print(f"{peso}")
    entrada2.delete(0, tk.END)
    return b

def altura(c):
    global altura
    altura = float (entrada3.get())
    print(f"{altura}")
    entrada3.delete(0, tk.END)
    return c

def imc():
    global imc
    imc = float (peso / altura**2)
    print(imc)
    resultado = tk.Toplevel(janela)
    resultado.title("Seu imc :D")
    resultado.geometry("400x200")
    resultado.configure(bg="#ffd209")

    label = tk.Label(resultado, text=f"Seu imc é: {imc}", bg="#ffd209", font=("Arial", 12))
    label.place(x=6, y=6)

    if imc < 18.4:
        oi = "Você está abaixo do peso"
        link_video = "https://i.imgur.com/EaEriv4.png"
        webbrowser.open(link_video)
    elif imc > 18.5 and imc <= 24.9:
        oi = "Peso normal"
        link_video = "https://i.imgur.com/Roa9Esa.png"
        webbrowser.open(link_video)
    elif imc > 25.0 and imc <= 29.9:
        oi = "Sobrepeso"
        link_video = "https://i.imgur.com/IEroxb1.png"
        webbrowser.open(link_video)
    elif imc > 30.0 and imc <= 34.9:
        oi = "Obesidade grau I"
        link_video = "https://i.imgur.com/DaEYDD1.png"
        webbrowser.open(link_video)
    elif imc > 35.0 and imc <= 39.9:
        oi = "Obesidade grau II"
        link_video = "https://i.imgur.com/fyNevkF.png"
        webbrowser.open(link_video)
    elif imc > 40:
        oi = "Obesidade grau III"
        link_video = "https://i.imgur.com/MYHpYCj.png"
        webbrowser.open(link_video)

    label2 = tk.Label(resultado, text=f"Seu imc é: {imc}", bg="#ffd209", font=("Arial", 12))
    label2.place(x=6, y=6)

    label_arquivo = tk.Label(resultado, text=f"{oi}", bg="#ffd209", font=("Arial", 12), wraplength=400)
    label_arquivo.place(x= 10, y=40)





janela = tk.Tk()
janela.title("Calculadora de imc")
janela.geometry("400x300")
janela.configure(bg="#ffd209")





label = tk.Label(janela, text="Coloque seu nome:", bg="#ffd209", font=("Arial", 12))
label.place(x=6, y =-2)

label2 = tk.Label(janela, text="Digite seu peso:", bg="#ffd209", font=("Arial", 12))
label2.place(x=6, y = 45)

label3 = tk.Label(janela, text="Digite sua altura:", bg="#ffd209", font=("Arial", 12))
label3.place(x=6, y = 100)



entrada = tk.Entry(janela, width=30, font=("Arial", 12))
entrada.place(x=10, y = 20)

entrada2 = tk.Entry(janela, width=30, font=("Arial", 12), validate = 'key')
entrada2.place(x=10, y = 70)

entrada3 = tk.Entry(janela, width=30, font=("Arial", 12), validate = 'key')
entrada3.place(x = 10, y = 125)



botao = tk.Button(janela, text="Enviar", command=lambda: nome(entrada), bg="#ff9100", fg="white", font=("Arial", 10, "bold"))
botao.place(x=300, y = 20)

botao3 = tk.Button(janela, text="Enviar", command=lambda: peso(entrada2), bg="#ff9100", fg="white", font=("Arial", 10, "bold"))
botao3.place(x=300, y = 68)

botao4 = tk.Button(janela, text="Enviar", command=lambda: altura(entrada3), bg="#ff9100", fg="white", font=("Arial", 10, "bold"))
botao4.place(x = 300, y = 122)

botao5 = tk.Button(janela, text="Ver imc", command=lambda: imc(), bg="#ff9100", fg="white", font=("Arial", 10, "bold"))
botao5.place(x = 300, y = 220)


janela.mainloop()