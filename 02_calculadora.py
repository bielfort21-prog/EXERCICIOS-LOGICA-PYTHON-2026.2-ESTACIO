# Questão 02 - Calculadora de operações aritméticas fundamentais

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Erro: informe um número válido.")

a = ler_numero("Primeiro número: ")
b = ler_numero("Segundo número: ")

print("\n=== RESULTADOS ===")
print(f"Adição       : {a + b}")
print(f"Subtração    : {a - b}")
print(f"Multiplicação: {a * b}")

if b == 0:
    print("Divisão      : Divisão por zero não permitida")
    print("Divisão inteira: Divisão por zero não permitida")
    print(f"Resto        : não calculado (divisor igual a zero)")
else:
    print(f"Divisão      : {a / b}")
    print(f"Divisão inteira: {a // b}")
    print(f"Resto        : {a % b}")

print(f"Potenciação  : {a ** b}")
