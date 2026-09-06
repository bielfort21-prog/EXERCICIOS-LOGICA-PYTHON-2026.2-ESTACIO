# Questão 12 - Cadastro e inventário de produtos
# Requisito: lista de dicionários.

produtos = []

print("=== CADASTRO DE PRODUTOS ===")
for i in range(1, 6):
    print(f"\nProduto {i}")
    while True:
        nome = input("Nome: ").strip()
        if nome:
            break
        print("Erro: informe o nome do produto.")

    while True:
        try:
            preco = float(input("Preço unitário: R$ ").replace(",", "."))
            if preco >= 0:
                break
            print("Erro: o preço não pode ser negativo.")
        except ValueError:
            print("Erro: informe um valor válido.")

    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade >= 0:
                break
            print("Erro: a quantidade não pode ser negativa.")
        except ValueError:
            print("Erro: informe um número inteiro.")

    produtos.append({
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

valor_total = sum(p["preco"] * p["quantidade"] for p in produtos)
produto_maior_preco = max(produtos, key=lambda p: p["preco"])

print("\n=== INVENTÁRIO ===")
for produto in produtos:
    subtotal = produto["preco"] * produto["quantidade"]
    print(f"{produto['nome']} | R$ {produto['preco']:.2f} | "
          f"Qtd.: {produto['quantidade']} | Subtotal: R$ {subtotal:.2f}")

print(f"\nValor total do estoque: R$ {valor_total:.2f}")
print(f"Produto com maior preço unitário: {produto_maior_preco['nome']} "
      f"(R$ {produto_maior_preco['preco']:.2f})")
