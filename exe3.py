"""Exercício 3: Tomada de Decisão (If/Elif/Else)
Crie um algoritmo para classificar o nível do Rio Negro e disparar alertas automáticos.
Peça ao usuário para digitar o nível atual do rio em metros (use input() e float()).
Se o nível for maior ou igual a 29.0 metros, imprima: "Alerta de Cheia Severa".
Se o nível for menor ou igual a 16.0 metros, imprima: "Alerta de Seca".
Caso contrário, imprima: "Nível Normal".
"""

niv_rio = float(input("Digite o nível atual do rio em metros:  "))

if niv_rio >= 29:
    print("Alerta de Cheia")
elif niv_rio <= 16:
    print("Alerta de Seca")
else:
    print("Normal")

