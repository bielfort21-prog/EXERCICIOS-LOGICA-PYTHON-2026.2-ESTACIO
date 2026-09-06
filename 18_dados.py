# Questão 18 - Simulação de lançamento de dados

import random

# Parte 1 - lançamento único
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("=== LANÇAMENTO ÚNICO ===")
print(f"Primeiro dado: {dado1}")
print(f"Segundo dado: {dado2}")
print(f"Soma: {dado1 + dado2}")

# Parte 2 - dez lançamentos
quantidade_soma_7 = 0

print("\n=== 10 LANÇAMENTOS ===")
for lancamento in range(1, 11):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    soma = d1 + d2

    print(f"Lançamento {lancamento}: dado 1 = {d1}, dado 2 = {d2}, soma = {soma}")

    if soma == 7:
        quantidade_soma_7 += 1

print(f"\nQuantidade de somas iguais a 7: {quantidade_soma_7}")
