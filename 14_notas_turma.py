# Questão 14 - Sistema de gerenciamento de notas da turma

def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero} (0 a 10): ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: informe um valor válido.")

def cadastrar_estudante(numero):
    nome = input(f"\nNome do estudante {numero}: ").strip()
    notas = [ler_nota(i) for i in range(1, 4)]
    media = sum(notas) / 3
    return {"nome": nome, "notas": notas, "media": media}

estudantes = [cadastrar_estudante(i) for i in range(1, 6)]

maior = max(estudantes, key=lambda e: e["media"])
menor = min(estudantes, key=lambda e: e["media"])
aprovados = sum(1 for e in estudantes if e["media"] >= 7)
recuperacao = sum(1 for e in estudantes if 5 <= e["media"] < 7)
reprovados = sum(1 for e in estudantes if e["media"] < 5)

print("\n=== RESULTADO DA TURMA ===")
for estudante in estudantes:
    print(f"{estudante['nome']}: média {estudante['media']:.2f}")

print(f"\nMaior média: {maior['nome']} ({maior['media']:.2f})")
print(f"Menor média: {menor['nome']} ({menor['media']:.2f})")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
