# Questão 19 - Análise linguística completa de uma frase

frase_original = input("Digite uma frase: ")
frase = " ".join(frase_original.split())

if not frase:
    print("Erro: a frase não pode estar vazia.")
else:
    palavras = frase.split()
    letra = input("Digite uma letra para contar as ocorrências: ").strip()

    while len(letra) != 1:
        print("Erro: informe exatamente uma letra.")
        letra = input("Digite uma letra: ").strip()

    ocorrencias = frase.casefold().count(letra.casefold())

    print("\n=== ANÁLISE DA FRASE ===")
    print(f"Total de caracteres (incluindo espaços): {len(frase)}")
    print(f"Quantidade de palavras: {len(palavras)}")
    print(f"Primeira palavra: {palavras[0]}")
    print(f"Última palavra: {palavras[-1]}")
    print(f"Ocorrências de '{letra}': {ocorrencias}")
    print(f"Maiúsculas: {frase.upper()}")
    print(f"Minúsculas: {frase.lower()}")
