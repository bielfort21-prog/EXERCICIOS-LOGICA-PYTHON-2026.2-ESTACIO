# Questão 05 - Classificação etária

while True:
    try:
        idade = int(input("Idade: "))
        if idade >= 0:
            break
        print("Erro: a idade não pode ser negativa.")
    except ValueError:
        print("Erro: informe um número inteiro.")

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"Classificação: {classificacao}")
