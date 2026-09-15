"""Questao 1. Crie um codigo que receba uma lista de entregas realizadas por dia em uma frota e retorne apenas os dados referentes aos ultimos 3 dias usando fatiamento (slicing). Dados de entrada: entregas_semana = [12, 45, 30, 50, 65, 20, 80]."""

entregas_semana = [12, 45, 30, 50, 65, 20, 80]
ultimos_tres_dias = entregas_semana[-3:]
print("Entregas dos últimos 3 dias:", ultimos_tres_dias)

"""Questao 2. Escreva um script em Python que pegue uma lista com o historico de FPS de uma partida de jogo e remova o primeiro e o ultimo registro utilizando slicing, retornando a lista intermediaria. Dados de entrada: fps_partida = [60, 59, 61, 58, 62, 60, 55]."""
fps_partida = [60, 59, 61, 58, 62, 60, 55]
fps_intermediario = fps_partida[1:-1]
print("FPS intermediário:", fps_intermediario)

"""Questao 3. Desenvolva uma funcao que receba um dicionario contendo o nome dos entregadores e a quantidade de rotas feitas, e retorne o nome do entregador que realizou mais rotas. Dados de entrada: rotas_entregadores = {'Ana': 15, 'Carlos': 22, 'Joao': 18}.""" 

def entregador_mais_eficiente(rotas_entregadores):
    return max(rotas_entregadores, key=rotas_entregadores.get)

rotas_entregadores = {'Ana': 15, 'Carlos': 22, 'Joao': 18}
entregador_top = entregador_mais_eficiente(rotas_entregadores)
print("Entregador que realizou mais rotas:", entregador_top)

