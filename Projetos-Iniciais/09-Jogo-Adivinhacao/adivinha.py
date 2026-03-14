import random  # Biblioteca para gerar números aleatórios

def jogo_adivinhacao():
    """
    Jogo de adivinhação de número.
    """

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("O computador vai escolher um número entre 1 e 100. Tente adivinhar!\n")

    while True:  # Loop principal para permitir jogar várias vezes
        numero_secreto = random.randint(1, 100)  # Número aleatório de 1 a 100
        tentativas = 0  # Contador de tentativas

        while True:  # Loop de tentativas
            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Por favor, digite apenas números inteiros.")
                continue

            tentativas += 1

            if palpite < numero_secreto:
                print("Mais alto!")  # Dica se o palpite é menor que o número secreto
            elif palpite > numero_secreto:
                print("Mais baixo!")  # Dica se o palpite é maior
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break  # Sai do loop de tentativas

        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").strip().lower()
        if jogar_novamente != "sim":
            print("Encerrando o jogo de adivinhação. Até mais!")
            break

# Executa o jogo
jogo_adivinhacao()
