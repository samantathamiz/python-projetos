# Banco de dados para Folha de Pagamento
# Criação das tabelas: funcionarios, dependentes, cargos, lotacoes

import sqlite3

def conectar():
    """
    Cria e retorna uma conexão com o banco folha.db
    """
    conn = sqlite3.connect("folha.db")
    return conn

def criar_tabelas():
    """
    Cria todas as tabelas necessárias no banco
    """
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de funcionários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        matricula INTEGER,
        cargo_id INTEGER,
        nivel INTEGER,
        lotacao TEXT,
        dependentes INTEGER,
        outros_descontos REAL
    )
    """)

    # Tabela de dependentes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dependentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        funcionario_id INTEGER,
        nome TEXT,
        idade INTEGER
    )
    """)

    # Tabela de cargos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cargos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        nivel1 REAL,
        nivel2 REAL,
        nivel3 REAL,
        nivel4 REAL,
        nivel5 REAL
    )
    """)

    # Tabela de lotações
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lotacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
    """)

    conn.commit()
    conn.close()

# Executa o arquivo diretamente para criar as tabelas
if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso!")
