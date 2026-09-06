# Questão 15 - Cadastro e análise populacional de cidades

cidades = []

for i in range(1, 6):
    print(f"\n=== Cidade {i} ===")
    nome = input("Nome: ").strip()

    while True:
        estado = input("Estado (sigla de 2 letras): ").strip().upper()
        if len(estado) == 2 and estado.isalpha():
            break
        print("Erro: informe uma sigla de estado com duas letras.")

    while True:
        try:
            populacao = int(input("População estimada: "))
            if populacao >= 0:
                break
            print("Erro: a população não pode ser negativa.")
        except ValueError:
            print("Erro: informe um número inteiro.")

    cidades.append({
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    })

maior = max(cidades, key=lambda cidade: cidade["populacao"])
menor = min(cidades, key=lambda cidade: cidade["populacao"])
total = sum(cidade["populacao"] for cidade in cidades)
media = total / len(cidades)

print("\n=== ANÁLISE POPULACIONAL ===")
print(f"Maior população: {maior['nome']} - {maior['populacao']:,}".replace(",", "."))
print(f"Menor população: {menor['nome']} - {menor['populacao']:,}".replace(",", "."))
print(f"População total: {total:,}".replace(",", "."))
print(f"Média populacional: {media:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

print("\nCidades cadastradas:")
for cidade in cidades:
    populacao = f"{cidade['populacao']:,}".replace(",", ".")
    print(f"- {cidade['nome']} - {cidade['estado']} - {populacao} habitantes")
