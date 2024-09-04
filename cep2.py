import tkinter as tk
from tkinter import messagebox
import requests

def buscar_endereco():
    state = entry_state.get().strip()
    city = entry_city.get().strip()
    street = entry_street.get().strip()
    
#    if len(state) != 2:
#        messagebox.showerror("Erro", "Digite um CEP válido de 8 dígitos.")
#        return

    url = f"https://viacep.com.br/ws/{state}/{city}/{street}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        dados = dados[0]
        
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            endereco = (
                f"CEP: {dados['cep']}\n"
            )
            label_resultado.config(text=endereco)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

# Configurando a janela principal
root = tk.Tk()
root.title("Busca de CEP pelo Endereço")
root.geometry("300x250")

# Campo de entrada para o CEP
label_state = tk.Label(root, text="Digite o Estado:")
label_state.pack(pady=5)
entry_state = tk.Entry(root)
entry_state.pack(pady=5)

label_city = tk.Label(root, text="Digite a Cidade:")
label_city.pack(pady=5)
entry_city = tk.Entry(root)
entry_city.pack(pady=5)

label_street = tk.Label(root, text="Digite a Rua:")
label_street.pack(pady=5)
entry_street = tk.Entry(root)
entry_street.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar Endereço", command=buscar_endereco)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()