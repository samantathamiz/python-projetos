def lista_de_tarefas_simples():
    """
    Lista de tarefas simples para iniciantes.
    """

    tarefas = []  # Lista que vai armazenar as tarefas

    while True:  # Loop principal do programa
        print("\nEscolha uma ação:")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Listar tarefas")
        print("4 - Sair")
        opcao = input("Digite o número da opção desejada: ").strip()

        # Adicionar tarefa
        if opcao == "1":
            tarefa = input("Digite a tarefa que deseja adicionar: ").strip()
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada.")

        # Remover tarefa
        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa para remover.")
                continue
            # Mostra as tarefas numeradas
            for i, t in enumerate(tarefas, 1):
                print(f"{i} - {t}")
            try:
                num = int(input("Digite o número da tarefa que deseja remover: "))
                if 1 <= num <= len(tarefas):
                    removida = tarefas.pop(num - 1)
                    print(f"Tarefa '{removida}' removida.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

        # Listar tarefas
        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa na lista.")
            else:
                print("\nTarefas:")
                for i, t in enumerate(tarefas, 1):
                    print(f"{i} - {t}")

        # Sair do programa
        elif opcao == "4":
            print("Encerrando a lista de tarefas. Até mais!")
            break

        # Opção inválida
        else:
            print("Opção inválida. Digite um número entre 1 e 4.")

# Executa a lista de tarefas simples
lista_de_tarefas_simples()
