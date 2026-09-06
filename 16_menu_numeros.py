# Questão 16 - Sistema interativo com menu de opções

numeros = []

while True:
    print("\n================================")
    print(" GERENCIAMENTO DE NÚMEROS")
    print("================================")
    print("1 - Cadastrar número")
    print("2 - Listar números")
    print("3 - Exibir maior número")
    print("4 - Exibir menor número")
    print("5 - Calcular média")
    print("0 - Encerrar programa")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        while True:
            try:
                numero = float(input("Digite o número: ").replace(",", "."))
                numeros.append(numero)
                print("Número cadastrado com sucesso.")
                break
            except ValueError:
                print("Erro: informe um número válido.")

    elif opcao == "2":
        if numeros:
            print("Números cadastrados:")
            for i, numero in enumerate(numeros, start=1):
                print(f"{i}. {numero:g}")
        else:
            print("Nenhum número cadastrado.")

    elif opcao in ("3", "4", "5"):
        if not numeros:
            print("Nenhum número cadastrado.")
        elif opcao == "3":
            print(f"Maior número: {max(numeros):g}")
        elif opcao == "4":
            print(f"Menor número: {min(numeros):g}")
        else:
            print(f"Média: {sum(numeros) / len(numeros):.2f}")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
