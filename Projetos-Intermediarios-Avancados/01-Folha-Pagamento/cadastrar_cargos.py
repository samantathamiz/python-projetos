# Cadastro de cargos com interface gráfica usando Tkinter

import sqlite3
import os
import tkinter as tk
from tkinter import messagebox, ttk

# Caminho do banco de dados:
dbname = os.path.join(os.path.dirname(__file__), "folha_pagamento.db")

# --- Funções do banco ---
def criar_tabela_cargos():
    """Cria a tabela de cargos se não existir"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cargos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            salario REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def listar_cargos():
    """Retorna lista com todos os cargos cadastrados"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, salario FROM cargos")
    cargos = cursor.fetchall()
    conn.close()
    return cargos

def cadastrar_cargo():
    """Cadastra um novo cargo no banco"""
    nome = entry_nome.get().strip()
    salario = entry_salario.get().strip()
    
    if not nome or not salario:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return
    
    try:
        salario = float(salario)
    except ValueError:
        messagebox.showwarning("Erro", "Digite um salário válido!")
        return
    
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cargos (nome, salario) VALUES (?, ?)", (nome, salario))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", f"Cargo '{nome}' cadastrado com sucesso!")
    
    entry_nome.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    
    atualizar_lista()

def atualizar_lista():
    """Atualiza a lista de cargos na Treeview"""
    for i in tree.get_children():
        tree.delete(i)
    for nome, salario in listar_cargos():
        tree.insert("", tk.END, values=(nome, salario))

# --- Configuração da janela ---
root = tk.Tk()
root.title("Cadastro de Cargos")
root.geometry("500x400")
root.resizable(False, False)

PADY_LABEL = 10
PADY_ENTRY = 5
ENTRY_WIDTH = 40

# Garante que a tabela existe
criar_tabela_cargos()

# Labels e campos
tk.Label(root, text="Nome do Cargo:").pack(pady=PADY_LABEL)
entry_nome = tk.Entry(root, width=ENTRY_WIDTH)
entry_nome.pack(pady=PADY_ENTRY)

tk.Label(root, text="Salário:").pack(pady=PADY_LABEL)
entry_salario = tk.Entry(root, width=ENTRY_WIDTH)
entry_salario.pack(pady=PADY_ENTRY)

# Botão para cadastrar
btn_cadastrar = tk.Button(root, text="Cadastrar Cargo", command=cadastrar_cargo,
                          bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_cadastrar.pack(pady=15)

# Treeview para listar cargos
tk.Label(root, text="Cargos cadastrados:").pack(pady=PADY_LABEL)
tree = ttk.Treeview(root, columns=("Nome", "Salário"), show="headings", height=10)
tree.heading("Nome", text="Nome")
tree.heading("Salário", text="Salário")
tree.column("Nome", width=250)
tree.column("Salário", width=100)
tree.pack(fill=tk.BOTH, expand=True, pady=10)

# Inicializa lista
atualizar_lista()

# Inicia a interface
root.mainloop()
