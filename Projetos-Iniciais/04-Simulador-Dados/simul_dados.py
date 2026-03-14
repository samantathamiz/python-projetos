import random  # Biblioteca para gerar números aleatórios

def simulador_dados():
    """
    Simulador de lançamento de dados.
    """

    while True:  # Loop principal para permitir repetir o lançamento
        try:
            quantidade = int(input("Quantos dados você deseja lançar? "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue  # Reinicia o loop se não for número

        # Lista para armazenar os resultados dos dados
        resultados = []

        # Lança os dados usando um loop
        for i in range(quantidade):
            dado = random.randint(1, 6)  # Gera número aleatório entre 1 e 6
            resultados.append(dado)       # Adiciona na lista
            print(f"Dado {i+1}: {dado}") # Mostra o resultado de cada dado

        # Calcula a média dos lançamentos
        media = sum(resultados) / len(resultados)
        print(f"Média dos resultados: {media:.2f}")

        # Pergunta se quer lançar os dados novamente
        outro = input("Deseja lançar os dados novamente? (sim/não): ").strip().lower()
        if outro != "sim":  # Sai do loop se não for "sim"
            print("Encerrando o simulador de dados. Até mais!")
            break

# Executa o simulador
simulador_dados()
