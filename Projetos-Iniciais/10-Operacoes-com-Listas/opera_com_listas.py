def operacoes_com_listas():
    """
    Programa simples para operações com listas de números.
    """

    lista = []  # Lista vazia para armazenar números

    while True:  # Loop principal do programa
        print("\nEscolha uma ação:")
        print("1 - Adicionar número à lista")
        print("2 - Remover número da lista")
        print("3 - Mostrar lista")
        print("4 - Mostrar soma, maior e menor número")
        print("5 - Sair")
        opcao = input("Digite o número da opção desejada: ").strip()

        # Adicionar número
        if opcao == "1":
            try:
                numero = float(input("Digite um número para adicionar: "))
                lista.append(numero)
                print(f"Número {numero} adicionado à lista.")
            except ValueError:
                print("Por favor, digite apenas números.")

        # Remover número
        elif opcao == "2":
            if not lista:
                print("A lista está vazia, não há números para remover.")
                continue
            print("Lista atual:", lista)
            try:
                numero = float(input("Digite o número que deseja remover: "))
                if numero in lista:
                    lista.remove(numero)
                    print(f"Número {numero} removido da lista.")
                else:
                    print("Número não encontrado na lista.")
            except ValueError:
                print("Por favor, digite apenas números.")

        # Mostrar lista
        elif opcao == "3":
            print("Lista atual:", lista)

        # Mostrar soma, maior e menor número
        elif opcao == "4":
            if not lista:
                print("A lista está vazia.")
            else:
                soma = sum(lista)
                maior = max(lista)
                menor = min(lista)
                print(f"Soma: {soma}, Maior: {maior}, Menor: {menor}")

        # Sair do programa
        elif opcao == "5":
            print("Encerrando o programa de operações com listas. Até mais!")
            break

        # Opção inválida
        else:
            print("Opção inválida. Digite um número entre 1 e 5.")

# Executa o programa
operacoes_com_listas()
