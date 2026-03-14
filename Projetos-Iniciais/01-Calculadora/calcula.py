def calculadora():
    # Loop infinito: o programa continua rodando até decidirmos parar
    while True:

        # Tenta pegar os números do usuário
        # Se o usuário digitar algo que não seja número, captura o erro
        try:
            num1 = float(input("Digite o primeiro número: "))  # Primeiro número
            num2 = float(input("Digite o segundo número: "))   # Segundo número
        except ValueError:
            print("Por favor, digite apenas números.")  # Mensagem de erro
            continue  # Volta pro começo do while

        # Pede ao usuário qual operação deseja fazer
        # .strip() remove espaços extras para evitar erro
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        # Verifica qual operação foi escolhida
        if operacao == '+':
            resultado = num1 + num2  # Adição
        elif operacao == '-':
            resultado = num1 - num2  # Subtração
        elif operacao == '*':
            resultado = num1 * num2  # Multiplicação
        elif operacao == '/':
            if num2 != 0:            # Verifica divisão por zero
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue  # Reinicia o loop
        else:
            print("Operação inválida. Tente novamente.")  # Qualquer outro caractere
            continue  # Reinicia o loop

        # Mostra o resultado
        print(f"O resultado é: {resultado}")

        # Pergunta se o usuário quer realizar outro cálculo
        outro_calculo = input("Deseja realizar outro cálculo? (sim/não): ").strip().lower()

        # Se a resposta não for 'sim', encerra a calculadora
        if outro_calculo != 'sim':
            print("Estamos encerrando a calculadora. Até mais!")
            break  # Sai do loop

# Executa a calculadora
calculadora()
