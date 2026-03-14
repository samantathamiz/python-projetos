import random  # Biblioteca para gerar valores aleatórios
import string  # Biblioteca para listas de letras, números e símbolos

def gerador_senha():
    """
    Gerador de senha aleatória.
    """

    while True:  # Loop principal para permitir gerar várias senhas
        try:
            tamanho = int(input("Digite o tamanho da senha que deseja gerar: "))
            if tamanho <= 0:
                print("O tamanho deve ser maior que zero.")
                continue
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        # Conjunto de caracteres que a senha pode conter
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # ascii_letters -> a-z A-Z
        # digits -> 0-9
        # punctuation -> !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        # Gera a senha aleatória
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        # Mostra a senha gerada
        print(f"Sua senha aleatória é: {senha}")

        # Pergunta se quer gerar outra senha
        outro = input("Deseja gerar outra senha? (sim/não): ").strip().lower()
        if outro != "sim":
            print("Encerrando o gerador de senhas. Até mais!")
            break

# Executa o gerador de senha
gerador_senha()
