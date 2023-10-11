import tkinter as tk
from tkinter import messagebox
import math

def m2_para_quantidade():
    try:
        m2 = float(entry_m2.get())
        m2_placa = 0.36
        calc = m2 / m2_placa
        calc = math.ceil(calc)
        resultado_label.config(text=f'O RESULTADO EM QUANTIDADE É: {calc} placas')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def quantidade_para_m2():
    try:
        qnt = int(entry_quantidade.get())
        m2_placa = 0.36
        calc = qnt * m2_placa
        calc = round(calc, 1)
        resultado_label.config(text=f'O RESULTADO EM M² É: {calc} metros quadrados')
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def sair():
    janela.quit()
    janela.destroy()

janela = tk.Tk()
janela.title("Conversor de Plaquinhas 60x60")

frame = tk.Frame(janela)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="QUAL CONVERSÃO DESEJA DESCOBRIR?")
label.grid(row=0, column=0, columnspan=2)

entry_m2 = tk.Entry(frame, width=10)
entry_m2.grid(row=1, column=0, padx=5, pady=5)
entry_m2_label = tk.Label(frame, text="M²")
entry_m2_label.grid(row=1, column=1, padx=5, pady=5)

entry_quantidade = tk.Entry(frame, width=10)
entry_quantidade.grid(row=2, column=0, padx=5, pady=5)
entry_quantidade_label = tk.Label(frame, text="Quantidade")
entry_quantidade_label.grid(row=2, column=1, padx=5, pady=5)

m2_button = tk.Button(frame, text="M² para Quantidade", command=m2_para_quantidade)
m2_button.grid(row=3, column=0, padx=5, pady=5)

quantidade_button = tk.Button(frame, text="Quantidade para M²", command=quantidade_para_m2)
quantidade_button.grid(row=3, column=1, padx=5, pady=5)

resultado_label = tk.Label(frame, text="", padx=10, pady=10)
resultado_label.grid(row=4, column=0, columnspan=2)

sair_button = tk.Button(frame, text="Sair", command=sair)
sair_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()
