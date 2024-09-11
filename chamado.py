import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import datetime
from datetime import date

# Função para criar o número do chamado
def gerar_numero_chamado():
        chamados = carregar_chamados()
        if chamados:
            ultimo_chamado = chamados [-1]['numero_chamado']
            return ultimo_chamado + 1
        return 1

# Função para salvar o pedido em um arquivo JSON
def salvar_chamado():
    ticket_number = 1
    user_name = entry_user.get()
    issue_tp = entry_issue.get()
    description = entry_describe.get()
    priority = entry_prior.get()
    date = date.today()

    if not user_name or not issue_tp or not description or not priority:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Estrutura do pedido
    chamado = {
            "numero_chamado": ticket_number,
            "cliente": user_name,
            "tipo_problema": issue_tp,
            "descricao": description,
            "prioridade": priority,
            "data_abertura": date
            }

    with open("chamados.json", "r") as arquivo:
        chamados = json.load(arquivo)

    # Adiciona o novo chamado
    chamados.append(chamado)

    # Salva chamado no Json
    with open("chamados.json", "w") as arquivo:
        json.dump(chamados, arquivo, indent=6)

    messagebox.showinfo("Sucesso", "Chamado submetido para análise")

    # Limpa os campos após salvar
    limpar_campos()

# Função para exibir um pedido específico
def recuperar_chamado():
    if os.path.exists("chamados.json"):
        user_name = simpledialog.askstring("Recuperar chamado", "Digite o número do chamado:")
        if not user_name:
            return

        with open("chamados.json", "r") as arquivo:
            chamados = json.load(arquivo)

        # Procura o chamado pelo número do chamado
        for chamado in chamados:
            if chamado["ticket_number"].lower() == ticket_number.lower():
                entry_user.delete(0, tk.END)
                entry_user.insert(0, chamado["cliente"])
                entry_quantidade.delete(0, tk.END)
                entry_quantidade.insert(0, pedido["quantidade"])
                entry_preco.delete(0, tk.END)
                entry_preco.insert(0, pedido["preco_unitario"])
                label_total_valor.config(text=f"R$ {pedido['preco_total']:.2f}")
                return

        messagebox.showinfo("Chamado não encontrado", f"Chamado número '{ticket_number}' não encontrado.")
    else:
        messagebox.showinfo("Sem chamados", "Nenhum chamado cadastrado até o momento.")

# Função para limpar os campos
def limpar_campos():
    entry_user.delete(0, tk.END)
    entry_issue.delete(0, tk.END)
    entry_describe.delete(0, tk.END)
    entry_prior.delete()
    entry_user.focus()

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Chamados de suporte técnico")

# Labels e Entries para os campos

label_ticketnum = tk.Label(janela, text="Número do chamado")
label_ticketnum.grid(row=0, column=0)

entry_user = tk.Entry(janela)
entry_user.grid(row=0, column=1)

label_user = tk.Label(janela, text="Nome do usuário")
label_user.grid(row=1, column=0)

entry_user = tk.Entry(janela)
entry_user.grid(row=1, column=1)

label_issue = tk.Label(janela, text="Tipo de problema")
label_issue.grid(row=2, column=0)

entry_issue = tk.Entry(janela)
entry_issue.grid(row=2, column=1)

label_describe = tk.Label(janela, text="Descrição do problema")
label_describe.grid(row=3, column=0)

entry_describe = tk.Entry(janela)
entry_describe.grid(row=3, column=1)

label_prior = tk.Label(janela, text="Prioridade")
label_prior.grid(row=4, column=0)

entry_prior = tk.Entry(janela)
entry_prior.grid(row=4, column=1)

label_date = tk.Label(janela, text="Data da solicitação")
label_date.grid(row=5, column=0)

day_today = date.today()
label_date_curr = tk.Label(janela, text=day_today.strftime('%d/%m/%Y'))
label_date_curr.grid(row=5, column=1)

# Botões organizados em duas linhas
botao_newticket = tk.Button(janela, text="Novo chamado", width=20, command=limpar_campos)
botao_newticket.grid(row=6, column=0)

botao_save = tk.Button(janela, text="Salvar chamado", width=20, command=salvar_chamado)
botao_save.grid(row=6, column=1)

botao_recuperar = tk.Button(janela, text="Localizar chamado", width=20, command=recuperar_chamado)
botao_recuperar.grid(row=7, column=0)

botao_novo_pedido = tk.Button(janela, text="Sair", width=20, command=janela.quit)
botao_novo_pedido.grid(row=7, column=1)

janela.mainloop()