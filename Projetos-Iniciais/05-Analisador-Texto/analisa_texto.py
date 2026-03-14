def analisador_texto():
    """
    Analisador de texto que conta letras, palavras e frases.
    """

    while True:  # Loop principal para permitir múltiplos textos
        # Pede o texto ao usuário
        texto = input("Digite o texto que deseja analisar: ")

        # Conta letras (apenas caracteres alfabéticos)
        letras = sum(1 for c in texto if c.isalpha())

        # Conta palavras (separadas por espaços)
        palavras = len(texto.split())

        # Conta frases (separadas por '.', '!' ou '?')
        frases = sum(texto.count(sep) for sep in ['.', '!', '?'])

        # Mostra os resultados
        print(f"Quantidade de letras: {letras}")
        print(f"Quantidade de palavras: {palavras}")
        print(f"Quantidade de frases: {frases}")

        # Pergunta se quer analisar outro texto
        outro = input("Deseja analisar outro texto? (sim/não): ").strip().lower()
        if outro != "sim":  # Sai do loop se não for "sim"
            print("Encerrando o analisador de texto. Até mais!")
            break

# Executa o analisador de texto
analisador_texto()
