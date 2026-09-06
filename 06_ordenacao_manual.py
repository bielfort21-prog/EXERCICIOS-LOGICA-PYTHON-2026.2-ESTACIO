# Questão 06 - Ordenação manual de três números
# Não utiliza max() nem min(). Os números devem ser distintos.

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: informe um número inteiro.")

while True:
    a = ler_inteiro("Primeiro número: ")
    b = ler_inteiro("Segundo número: ")
    c = ler_inteiro("Terceiro número: ")

    if a != b and a != c and b != c:
        break
    print("Erro: os três números devem ser distintos.\n")

# Comparações condicionais aninhadas para descobrir maior e menor.
if a > b:
    if a > c:
        maior = a
        if b > c:
            medio, menor = b, c
        else:
            medio, menor = c, b
    else:
        maior = c
        medio, menor = a, b
else:
    if b > c:
        maior = b
        if a > c:
            medio, menor = a, c
        else:
            medio, menor = c, a
    else:
        maior = c
        medio, menor = b, a

print(f"\nMaior: {maior}")
print(f"Mediano: {medio}")
print(f"Menor: {menor}")
