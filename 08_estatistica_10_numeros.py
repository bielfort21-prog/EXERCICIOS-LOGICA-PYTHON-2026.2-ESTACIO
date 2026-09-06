# Questão 08 - Estatística descritiva de 10 números

numeros = []

for i in range(1, 11):
    while True:
        try:
            numero = int(input(f"Digite o {i}º número inteiro: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Erro: informe um número inteiro.")

soma = sum(numeros)
positivos = sum(1 for n in numeros if n > 0)
negativos = sum(1 for n in numeros if n < 0)
pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)
media = soma / len(numeros)

print("\n=== RELATÓRIO ESTATÍSTICO ===")
print(f"Soma: {soma}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Média: {media:.2f}")
