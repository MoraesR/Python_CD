"""Análise em Lote (For Loop)
Você recebeu uma lista com as temperaturas máximas diárias da última semana: temperaturas = [31.5, 33.2, 34.0, 32.8, 35.1, 34.5, 33.9] Usando um laço for:
Identifique e imprima a temperatura máxima registrada na semana (sem usar a função nativa max()).
Calcule e imprima a média térmica da semana.
"""



temperaturas = [31.5, 33.2, 34.0, 32.8, 35.1, 34.5, 33.9]
maior_temperatura = temperaturas [0]
soma_temperatura = 0

for temp in temperaturas:
    if temp > maior_temperatura:
        maior_temperatura = temp

    soma_temperatura += temp

quantidade_dias = len(temperaturas)
media_termica = soma_temperatura / quantidade_dias

print(f"Temperatura máxima registrada na semana: {maior_temperatura}°C")
print(f"Média térmica da semana: {media_termica:.2f}°C")

    