import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("Teste",f"{entryNome.get()};\ntel:{entryTelefone.get()}")

janela = tk.Tk()
janela.title("Cadastro de cliente")

# **** Cadastro do nome do cliente ****
labelNome = tk.Label(janela,text="Nome",font=("Arial", 16), fg="black", bg="yellow")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela)
entryNome.pack(padx=50, pady=5)

# ****Cadastro do telefone do
labelTelefone = tk.Label(janela,text="Telefone")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela)
entryTelefone.pack(padx=50, pady=5)

# **** Cadastro do e-mail do cliente ****
labelEmail = tk.Label(janela,text="E-mail")
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, text="Salvar")
entryEmail.pack(padx=50, pady=5)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=50, pady=5)

janela.geometry("400x300")

janela.mainloop()
