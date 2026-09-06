# Questão 17 - Cálculos matemáticos com o módulo math

import math

while True:
    try:
        numero = float(input("Digite um número real: ").replace(",", "."))
        break
    except ValueError:
        print("Erro: informe um número válido.")

print("\n=== CÁLCULOS MATEMÁTICOS ===")

if numero >= 0:
    print(f"Raiz quadrada: {math.sqrt(numero):.4f}")
else:
    print("Raiz quadrada: não existe nos números reais.")

print(f"Valor absoluto: {math.fabs(numero):.4f}")
print(f"Teto (ceil): {math.ceil(numero)}")
print(f"Piso (floor): {math.floor(numero)}")

if numero.is_integer() and numero >= 0:
    print(f"Fatorial: {math.factorial(int(numero))}")
else:
    print("Fatorial: disponível somente para número inteiro e não negativo.")
