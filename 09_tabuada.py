# Questão 09 - Tabuada de multiplicação

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro: informe um número inteiro.")

print(f"\n=== TABUADA DO {numero} ===")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
