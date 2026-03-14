def agenda_contatos_simples():
    """
    Agenda de contatos simples para iniciantes.
    """

    contatos = []  # Lista que vai armazenar os contatos como tuplas (nome, telefone)

    while True:  # Loop principal do programa
        print("\nEscolha uma ação:")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Listar contatos")
        print("4 - Sair")
        opcao = input("Digite o número da opção desejada: ").strip()

        # Adicionar contato
        if opcao == "1":
            nome = input("Digite o nome do contato: ").strip()
            telefone = input("Digite o telefone do contato: ").strip()
            contatos.append((nome, telefone))  # Armazena como tupla
            print(f"Contato '{nome}' adicionado com telefone {telefone}.")

        # Remover contato
        elif opcao == "2":
            if not contatos:
                print("Nenhum contato para remover.")
                continue
            # Mostra os contatos numerados
            for i, (nome, telefone) in enumerate(contatos, 1):
                print(f"{i} - {nome}: {telefone}")
            try:
                num = int(input("Digite o número do contato que deseja remover: "))
                if 1 <= num <= len(contatos):
                    removido = contatos.pop(num - 1)
                    print(f"Contato '{removido[0]}' removido.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

        # Listar contatos
        elif opcao == "3":
            if not contatos:
                print("Nenhum contato na agenda.")
            else:
                print("\nContatos:")
                for i, (nome, telefone) in enumerate(contatos, 1):
                    print(f"{i} - {nome}: {telefone}")

        # Sair do programa
        elif opcao == "4":
            print("Encerrando a agenda de contatos. Até mais!")
            break

        # Opção inválida
        else:
            print("Opção inválida. Digite um número entre 1 e 4.")

# Executa a agenda de contatos simples
agenda_contatos_simples()
