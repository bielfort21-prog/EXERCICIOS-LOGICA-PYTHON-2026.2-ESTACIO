# Questão 20 - Sistema completo de gerenciamento acadêmico

def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: informe um inteiro positivo.")
        except ValueError:
            print("Erro: informe um número inteiro.")

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: informe uma nota válida.")

def calcular_situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"

def criar_estudante():
    nome = input("Nome: ").strip()
    idade = ler_inteiro_positivo("Idade: ")
    curso = input("Curso: ").strip()
    notas = [ler_nota(f"Nota {i}: ") for i in range(1, 4)]
    media = sum(notas) / 3

    return {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": calcular_situacao(media)
    }

def exibir_estudante(estudante):
    print(f"Nome: {estudante['nome']}")
    print(f"Idade: {estudante['idade']}")
    print(f"Curso: {estudante['curso']}")
    print("Notas:", ", ".join(f"{nota:.2f}" for nota in estudante["notas"]))
    print(f"Média: {estudante['media']:.2f}")
    print(f"Situação: {estudante['situacao']}")

def encontrar_estudante(estudantes, nome):
    for estudante in estudantes:
        if estudante["nome"].casefold() == nome.casefold():
            return estudante
    return None

def listar_estudantes(estudantes):
    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return

    print("\n=== ESTUDANTES CADASTRADOS ===")
    for estudante in estudantes:
        print("-" * 35)
        exibir_estudante(estudante)
    print("-" * 35)

def consultar_estudante(estudantes):
    nome = input("Nome para consulta: ").strip()
    estudante = encontrar_estudante(estudantes, nome)

    if estudante:
        print("\n=== DADOS DO ESTUDANTE ===")
        exibir_estudante(estudante)
    else:
        print("Estudante não encontrado.")

def alterar_estudante(estudantes):
    nome = input("Nome do estudante que deseja alterar: ").strip()
    estudante = encontrar_estudante(estudantes, nome)

    if not estudante:
        print("Estudante não encontrado.")
        return

    print("\nPressione Enter para manter o valor atual.")

    novo_nome = input(f"Nome [{estudante['nome']}]: ").strip()
    if novo_nome:
        estudante["nome"] = novo_nome

    nova_idade = input(f"Idade [{estudante['idade']}]: ").strip()
    if nova_idade:
        try:
            nova_idade = int(nova_idade)
            if nova_idade > 0:
                estudante["idade"] = nova_idade
            else:
                print("Idade inválida; valor mantido.")
        except ValueError:
            print("Idade inválida; valor mantido.")

    novo_curso = input(f"Curso [{estudante['curso']}]: ").strip()
    if novo_curso:
        estudante["curso"] = novo_curso

    for i in range(3):
        atual = estudante["notas"][i]
        nova_nota = input(f"Nota {i + 1} [{atual:.2f}]: ").strip()
        if nova_nota:
            try:
                valor = float(nova_nota.replace(",", "."))
                if 0 <= valor <= 10:
                    estudante["notas"][i] = valor
                else:
                    print("Nota inválida; valor mantido.")
            except ValueError:
                print("Nota inválida; valor mantido.")

    estudante["media"] = sum(estudante["notas"]) / 3
    estudante["situacao"] = calcular_situacao(estudante["media"])

    print("Dados alterados com sucesso.")

def remover_estudante(estudantes):
    nome = input("Nome do estudante que deseja remover: ").strip()
    estudante = encontrar_estudante(estudantes, nome)

    if not estudante:
        print("Estudante não encontrado.")
        return

    confirmacao = input(
        f"Confirma a remoção de {estudante['nome']}? (s/n): "
    ).strip().lower()

    if confirmacao == "s":
        estudantes.remove(estudante)
        print("Estudante removido com sucesso.")
    else:
        print("Remoção cancelada.")

def gerar_relatorio(estudantes):
    if not estudantes:
        print("Nenhum estudante cadastrado.")
        return

    maior = max(estudantes, key=lambda e: e["media"])
    menor = min(estudantes, key=lambda e: e["media"])
    media_geral = sum(e["media"] for e in estudantes) / len(estudantes)
    aprovados = sum(1 for e in estudantes if e["situacao"] == "Aprovado")
    recuperacao = sum(1 for e in estudantes if e["situacao"] == "Recuperação")
    reprovados = sum(1 for e in estudantes if e["situacao"] == "Reprovado")

    print("\n========================================")
    print("       RELATÓRIO DA TURMA")
    print("========================================")
    print(f"Total de estudantes: {len(estudantes)}")
    print(f"Maior média: {maior['nome']} ({maior['media']:.2f})")
    print(f"Menor média: {menor['nome']} ({menor['media']:.2f})")
    print(f"Média geral: {media_geral:.2f}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")

def menu():
    estudantes = []

    while True:
        print("\n========================================")
        print("          SISTEMA ACADÊMICO")
        print("========================================")
        print("1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("3 - Consultar estudante")
        print("4 - Alterar dados")
        print("5 - Remover estudante")
        print("6 - Gerar relatório da turma")
        print("0 - Encerrar sistema")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            estudantes.append(criar_estudante())
            print("Estudante cadastrado com sucesso.")
        elif opcao == "2":
            listar_estudantes(estudantes)
        elif opcao == "3":
            consultar_estudante(estudantes)
        elif opcao == "4":
            alterar_estudante(estudantes)
        elif opcao == "5":
            remover_estudante(estudantes)
        elif opcao == "6":
            gerar_relatorio(estudantes)
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
