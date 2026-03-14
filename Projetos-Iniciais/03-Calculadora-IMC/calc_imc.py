def calculadora_imc():
    """
    Calculadora de IMC (Índice de Massa Corporal)
    """
    while True:  # Loop principal: repete até o usuário decidir sair

        # Pede o peso do usuário em kg
        try:
            peso = float(input("Digite seu peso em kg: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue  # Reinicia o loop

        # Pede a altura do usuário em metros
        try:
            altura = float(input("Digite sua altura em metros: "))
        except ValueError:
            print("Por favor, digite apenas números.")
            continue  # Reinicia o loop

        # Calcula o IMC
        imc = peso / (altura ** 2)

        # Classifica o IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            classificacao = "Peso normal"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        # Mostra o resultado
        print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

        # Pergunta se quer calcular outro IMC
        outro = input("Deseja calcular outro IMC? (sim/não): ").strip().lower()
        if outro != "sim":
            print("Encerrando a calculadora de IMC. Até mais!")
            break

# Executa a calculadora de IMC
calculadora_imc()
