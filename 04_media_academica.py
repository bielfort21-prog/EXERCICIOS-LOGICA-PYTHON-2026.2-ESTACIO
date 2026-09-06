# Questão 04 - Cálculo de média e situação acadêmica

def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero} (0 a 10): ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: informe um valor numérico.")

notas = [ler_nota(i) for i in range(1, 4)]
media = sum(notas) / len(notas)

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n=== RESULTADO ACADÊMICO ===")
print(f"Notas: {notas[0]:.2f}, {notas[1]:.2f}, {notas[2]:.2f}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
