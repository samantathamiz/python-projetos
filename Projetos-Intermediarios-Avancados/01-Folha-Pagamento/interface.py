# Interface

import sqlite3
import os
import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF
from datetime import datetime
from calculos import calcular_salario_liquido

# Caminho do banco de dados
dbname = os.path.join(os.path.dirname(__file__), "folha_pagamento.db")

# --- Funções de banco ---
def criar_tabela_cargos():
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

def criar_tabela_funcionarios():
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def listar_cargos():
    """Retorna todos os cargos cadastrados"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM cargos")
    cargos = [row[0] for row in cursor.fetchall()]
    conn.close()
    return cargos

def pegar_salario_cargo(cargo):
    """Retorna o salário do cargo selecionado"""
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT salario FROM cargos WHERE nome = ?", (cargo,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0.0

# --- Funções de funcionário ---
def cadastrar_funcionario():
    nome = entry_nome.get().strip()
    cargo = combo_cargo.get()
    salario = entry_salario.get().strip()

    if not nome or not cargo:
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    try:
        salario = float(salario)
    except ValueError:
        messagebox.showwarning("Erro", "Salário inválido!")
        return

    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)",
                   (nome, cargo, salario))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", f"Funcionário '{nome}' cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    combo_cargo.set('')
    entry_salario.delete(0, tk.END)

    atualizar_lista()

def atualizar_lista():
    """Atualiza a Treeview com todos os funcionários"""
    for i in tree.get_children():
        tree.delete(i)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cargo, salario FROM funcionarios")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()

def atualizar_salario(event):
    """Atualiza o campo de salário ao selecionar um cargo"""
    cargo = combo_cargo.get()
    salario = pegar_salario_cargo(cargo)
    entry_salario.delete(0, tk.END)
    entry_salario.insert(0, str(salario))

# --- Função para gerar a folha de pagamento ---
def gerar_folha():
    """Gera a folha de pagamento em PDF para o funcionário selecionado"""
    selecionado = tree.focus()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um funcionário na lista!")
        return

    nome, cargo, salario = tree.item(selecionado, 'values')
    salario = float(salario)

    # Calcula salários e descontos usando calculos.py
    resultados = calcular_salario_liquido(salario)
    salario_bruto = resultados["salario_bruto"]
    imposto_talisma = resultados["imposto_talisma"]
    imposto_mistico = resultados["imposto_mistico"]
    salario_liquido = resultados["salario_liquido"]

    # Criar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Folha de Pagamento", 0, 1, 'C')

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Nome: {nome}", 0, 1)
    pdf.cell(0, 10, f"Cargo: {cargo}", 0, 1)
    pdf.cell(0, 10, f"Salário Bruto: R$ {salario_bruto:.2f}", 0, 1)
    pdf.cell(0, 10, f"Imposto Talismã: R$ {imposto_talisma:.2f}", 0, 1)
    pdf.cell(0, 10, f"Imposto Místico: R$ {imposto_mistico:.2f}", 0, 1)
    pdf.cell(0, 10, f"Salário Líquido: R$ {salario_liquido:.2f}", 0, 1)
    pdf.ln(10)
    pdf.cell(0, 10, f"Emitido em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", 0, 1)

    # Salva PDF na mesma pasta do projeto
    caminho_pdf = os.path.join(os.path.dirname(__file__), f"Folha{nome.replace(' ', '_')}.pdf")
    pdf.output(caminho_pdf)

    messagebox.showinfo("Folha gerada", f"Folha de pagamento gerada:\n{caminho_pdf}")

# --- Configuração da janela ---
root = tk.Tk()
root.title("Cadastro de Funcionários")
root.geometry("700x550")
root.resizable(False, False)

PADY_LABEL = 10
PADY_ENTRY = 5
ENTRY_WIDTH = 50

# Cria tabelas caso não existam
criar_tabela_cargos()
criar_tabela_funcionarios()

# Labels e campos
tk.Label(root, text="Nome do Funcionário:").pack(pady=PADY_LABEL)
entry_nome = tk.Entry(root, width=ENTRY_WIDTH)
entry_nome.pack(pady=PADY_ENTRY)

tk.Label(root, text="Cargo:").pack(pady=PADY_LABEL)
combo_cargo = ttk.Combobox(root, width=ENTRY_WIDTH, values=listar_cargos())
combo_cargo.pack(pady=PADY_ENTRY)
combo_cargo.bind("<<ComboboxSelected>>", atualizar_salario)

tk.Label(root, text="Salário:").pack(pady=PADY_LABEL)
entry_salario = tk.Entry(root, width=ENTRY_WIDTH)
entry_salario.pack(pady=PADY_ENTRY)

# Botões
btn_salvar = tk.Button(root, text="Cadastrar Funcionário", command=cadastrar_funcionario,
                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_salvar.pack(pady=10)

btn_gerar = tk.Button(root, text="Gerar Folha de Pagamento", command=gerar_folha,
                       bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_gerar.pack(pady=10)

# Treeview para exibir funcionários cadastrados
tk.Label(root, text="Funcionários cadastrados:").pack(pady=PADY_LABEL)
tree = ttk.Treeview(root, columns=("Nome", "Cargo", "Salário"), show="headings", height=12)
tree.heading("Nome", text="Nome")
tree.heading("Cargo", text="Cargo")
tree.heading("Salário", text="Salário")
tree.column("Nome", width=250)
tree.column("Cargo", width=150)
tree.column("Salário", width=100)
tree.pack(fill=tk.BOTH, expand=True, pady=10)

# Inicializa lista
atualizar_lista()

root.mainloop()
