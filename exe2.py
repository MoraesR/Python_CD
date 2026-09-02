###Exercício 2: Tuplas e Imutabilidade
#Um sensor GPS envia dados de localização que não podem ser alterados pelo sistema.
#Crie uma tupla chamada coordenadas com os valores de latitude e longitude: (-3.1190, -60.0217).
#Tente alterar o valor da latitude para -3.1200 (observe o erro que o Python irá gerar, provando a imutabilidade).
#Desempacote a tupla em duas variáveis: lat e lon.
#Imprima formatado: "A latitude registrada é X e a longitude é Y".
###

coordenadas = (-3.1190, -60.0217)
print(coordenadas)
#coordenadas[0] = -3.1200  <-- Se descomentar essa linha, o programa quebra!

lat, lon = coordenadas
print(f"A latitude registrada é {lat} e a longitude é {lon}.")
