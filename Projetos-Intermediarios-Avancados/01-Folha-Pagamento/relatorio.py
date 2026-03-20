# Tela de relatório de funcionários usando Tkinter

import sqlite3
import os
import tkinter as tk
from tkinter import ttk

# Caminho do banco de dados
dbname = os.path.join(os.path.dirname(__file__), "folha_pagamento.db")

# --- Funções ---
def listar_funcionarios():
    """Retorna todos os funcionários cadastrados"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cargo, salario FROM funcionarios")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_lista():
    """Atualiza a Treeview com todos os funcionários"""
    for i in tree.get_children():
        tree.delete(i)
    for row in listar_funcionarios():
        tree.insert("", tk.END, values=row)

# --- Configuração da janela ---
root = tk.Tk()
root.title("Relatório de Funcionários")
root.geometry("650x500")
root.resizable(False, False)

PADY_LABEL = 10

# Label
tk.Label(root, text="Funcionários cadastrados:", font=("Arial", 12, "bold")).pack(pady=PADY_LABEL)

# Treeview
tree = ttk.Treeview(root, columns=("Nome", "Cargo", "Salário"), show="headings", height=15)
tree.heading("Nome", text="Nome")
tree.heading("Cargo", text="Cargo")
tree.heading("Salário", text="Salário")
tree.column("Nome", width=200)
tree.column("Cargo", width=150)
tree.column("Salário", width=100)
tree.pack(fill=tk.BOTH, expand=True, pady=10)

# Botão atualizar
btn_atualizar = tk.Button(root, text="Atualizar Lista", command=atualizar_lista,
                          bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_atualizar.pack(pady=10)

# Inicializa a lista
atualizar_lista()

# Inicia a interface
root.mainloop()
