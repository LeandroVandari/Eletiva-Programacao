import tkinter as tk

def inserir_texto(x):
    texto.insert(1.0, x)

janela = tk.Tk()
janela.geometry("400x400")

texto = tk.Text(janela, height=4, width=16, font=("Arial", 24))
texto.grid(columnspan=4)

botao1 = tk.Button(janela, text="1", command=lambda: inserir_texto("1"), width=3, height=3, font=("Arial", 12))
botao1.grid(column=0, row=1)


janela.mainloop()
