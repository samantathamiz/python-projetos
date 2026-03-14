def mini_quiz():
    """
    Mini quiz de perguntas e respostas.
    """

    # Lista de perguntas e respostas corretas (pergunta, resposta)
    perguntas = [
        ("Qual é a capital do Brasil?", "Brasília"),
        ("Quantos dias tem uma semana?", "7"),
        ("Qual é o maior planeta do Sistema Solar?", "Júpiter")
    ]

    while True:  # Loop principal para repetir o quiz se o usuário quiser
        print("\nBem-vindo ao mini quiz!\n")
        pontuacao = 0  # Contador de respostas corretas

        # Pergunta cada questão
        for pergunta, resposta_correta in perguntas:
            resposta = input(pergunta + " ").strip()  # Recebe a resposta do usuário
            if resposta.lower() == resposta_correta.lower():  # Compara ignorando maiúsculas/minúsculas
                print("Correto!")
                pontuacao += 1
            else:
                print(f"Errado! A resposta correta é: {resposta_correta}")

        # Mostra a pontuação final
        print(f"\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.")

        # Pergunta se o usuário quer jogar novamente
        outro = input("Deseja tentar novamente? (sim/não): ").strip().lower()
        if outro != "sim":
            print("Encerrando o mini quiz. Até mais!")
            break

# Executa o mini quiz
mini_quiz()
