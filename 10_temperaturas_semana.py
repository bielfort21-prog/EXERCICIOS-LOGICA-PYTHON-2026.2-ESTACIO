# Questão 10 - Análise de temperaturas de uma semana

temperaturas = []

for dia in range(1, 8):
    while True:
        try:
            temperatura = float(input(f"Temperatura do dia {dia}: ").replace(",", "."))
            temperaturas.append(temperatura)
            break
        except ValueError:
            print("Erro: informe uma temperatura válida.")

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / len(temperaturas)
acima_da_media = sum(1 for temperatura in temperaturas if temperatura > media)

print("\n=== RELATÓRIO DA SEMANA ===")
print("Temperaturas:", ", ".join(f"{t:.2f} °C" for t in temperaturas))
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Menor temperatura: {menor:.2f} °C")
print(f"Temperatura média: {media:.2f} °C")
print(f"Dias acima da média: {acima_da_media}")
