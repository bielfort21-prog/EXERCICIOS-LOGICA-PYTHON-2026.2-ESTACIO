# Questão 03 - Conversão entre escalas termométricas

while True:
    try:
        celsius = float(input("Temperatura em Celsius: ").replace(",", "."))
        break
    except ValueError:
        print("Erro: informe um valor numérico.")

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print("\n=== CONVERSÃO ===")
print(f"Celsius   : {celsius:.2f} °C")
print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin    : {kelvin:.2f} K")
