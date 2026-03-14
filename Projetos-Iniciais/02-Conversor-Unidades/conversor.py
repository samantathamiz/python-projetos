def conversor_celsius_fahrenheit():
    while True:  # Loop principal: repete até o usuário decidir sair

        # Pergunta qual tipo de conversão
        print("Escolha o tipo de conversão:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        opcao = input("Digite 1 ou 2: ").strip()

        # Verifica se a opção digitada é válida
        if opcao not in ["1", "2"]:
            print("Opção inválida. Digite 1 ou 2.")
            continue  # Reinicia o loop

        # Pede o valor da temperatura
        try:
            valor = float(input("Digite a temperatura que deseja converter: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue  # Reinicia o loop

        # Converte de acordo com a opção
        if opcao == "1":  # Celsius para Fahrenheit
            resultado = (valor * 9/5) + 32
            print(f"{valor} graus Celsius equivalem a {resultado:.2f} graus Fahrenheit")
        elif opcao == "2":  # Fahrenheit para Celsius
            resultado = (valor - 32) * 5/9
            print(f"{valor} graus Fahrenheit equivalem a {resultado:.2f} graus Celsius")

        # Pergunta se quer fazer outra conversão
        outro = input("Deseja realizar outra conversão? (sim/não): ").strip().lower()
        if outro != "sim":  # Sai do loop se não for "sim"
            print("Programa encerrado. Tchau, até mais!")
            break

# Executa o conversor
conversor_celsius_fahrenheit()
