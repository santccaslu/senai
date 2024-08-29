import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mensagem():
    messagebox.showinfo("Aviso!",f"Cadastro do {entryPet.get()} efetuado!")

janela = tk.Tk()
janela.title("Cadastro do animal")

# Cadastro do tutor
labelTutor = tk.Label(janela,text="Nome do tutor")
labelTutor.pack(padx=50, pady=5)

entryTutor = tk.Entry(janela)
entryTutor.pack(padx=50, pady=5)

# Cadastro do Pet
labelPet = tk.Label(janela,text="Nome do Pet")
labelPet.pack(padx=50, pady=5)

entryPet = tk.Entry(janela)
entryPet.pack(padx=50, pady=5)

# Data de nascimento do Pet
labelBirth = tk.Label(janela,text="Data de nascimento do pet")
labelBirth.pack(padx=50, pady=5)

entryBirth = tk.Entry(janela)
entryBirth.pack(padx=50, pady=5)

# Espécie do Pet
labelSpec = tk.Label(janela,text="Espécie do pet")
labelSpec.pack(padx=50, pady=5)

combo = ttk.Combobox(janela)
combo["values"]= ("","Cachorro", "Gato", "Galinha")
combo.current(0)
combo.pack(padx=50, pady=5)

# Raça do Pet
labelRace = tk.Label(janela,text="Raça do pet")
labelRace.pack(padx=50, pady=5)

entryRace = tk.Entry(janela)
entryRace.pack(padx=50, pady=5)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=50, pady=5)

janela.geometry("400x400")

janela.mainloop()