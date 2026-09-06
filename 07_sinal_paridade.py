# Questão 07 - Análise simultânea de sinal e paridade

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Erro: informe um número inteiro.")

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "nulo"

paridade = "par" if numero % 2 == 0 else "ímpar"

print(f"O número {numero} é {sinal} e {paridade}.")
