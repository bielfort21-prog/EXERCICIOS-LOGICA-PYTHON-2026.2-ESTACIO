# Questão 01 - Cadastro e apresentação de perfil pessoal

def ler_idade():
    while True:
        try:
            idade = int(input("Idade: "))
            if idade >= 0:
                return idade
            print("Erro: a idade não pode ser negativa.")
        except ValueError:
            print("Erro: informe um número inteiro.")

def ler_altura():
    while True:
        try:
            altura = float(input("Altura (m): ").replace(",", "."))
            if altura > 0:
                return altura
            print("Erro: a altura deve ser positiva.")
        except ValueError:
            print("Erro: informe um valor numérico.")

print("\n=== CADASTRO DE PERFIL ===")
nome = input("Nome completo: ").strip()
idade = ler_idade()
altura = ler_altura()
cidade = input("Cidade onde reside: ").strip()

print("\n" + "=" * 35)
print("      CARTÃO DE IDENTIFICAÇÃO")
print("=" * 35)
print(f"Nome   : {nome}")
print(f"Idade  : {idade} anos")
print(f"Altura : {altura:.2f} m")
print(f"Cidade : {cidade}")
print("=" * 35)
