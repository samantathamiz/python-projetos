# Arquivo principal da Folha de Pagamento
# Responsável por iniciar o sistema

import tkinter as tk
from database import criar_tabelas
import interface                        # importa a interface principal do sistema

def main():
    """
    Função principal que cria as tabelas e inicia a interface
    """
    # Criar tabelas se ainda não existirem
    criar_tabelas()

    # Inicializa a interface principal
    interface.root.mainloop()


# Ao rodar o arquivo diretamente, chama a função main
if __name__ == "__main__":
    main()
