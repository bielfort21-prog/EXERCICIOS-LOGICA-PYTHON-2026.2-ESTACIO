# Questão 11 - Relatório analítico de lista numérica

numeros = []

for i in range(1, 11):
    while True:
        try:
            numeros.append(int(input(f"Digite o {i}º número inteiro: ")))
            break
        except ValueError:
            print("Erro: informe um número inteiro.")

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\n=== RELATÓRIO ===")
print(f"Números informados: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Soma: {sum(numeros)}")
print(f"Média: {sum(numeros) / len(numeros):.2f}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
