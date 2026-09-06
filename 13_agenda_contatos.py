# Questão 13 - Agenda de contatos
# Requisito: lista de dicionários.

contatos = []

print("=== AGENDA DE CONTATOS ===")
for i in range(1, 6):
    print(f"\nContato {i}")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()

    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })

consulta = input("\nDigite o nome para consultar: ").strip()

contato_encontrado = None
for contato in contatos:
    if contato["nome"].casefold() == consulta.casefold():
        contato_encontrado = contato
        break

if contato_encontrado:
    print("\n=== CONTATO ENCONTRADO ===")
    print(f"Nome: {contato_encontrado['nome']}")
    print(f"Telefone: {contato_encontrado['telefone']}")
    print(f"E-mail: {contato_encontrado['email']}")
else:
    print("Contato não encontrado.")
