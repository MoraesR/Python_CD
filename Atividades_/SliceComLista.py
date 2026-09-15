"""
Exemplo de Slicing (Fatiamento) de Listas
Contexto: Analisando o log de fases testadas no QA de um jogo
"""

# Lista representando os IDs das fases que já passaram pelo teste de QA
fases_testadas = ['Fase_01', 'Fase_02', 'Fase_03', 'Fase_04', 'Fase_05', 'Fase_06']
# Índices Positivos:    0           1           2           3           4           5
# Índices Negativos:   -6          -5          -4          -3          -2          -1

print("Lista original:", fases_testadas)
print("-" * 40)

# 1. Fatiamento Básico [start:stop]
# Pega do índice 1 até o 3 (Lembre-se: o índice 4 fica de fora!)
print("1. Fases do meio [1:4]:")
print(fases_testadas[1:4])  
# Saída: ['Fase_02', 'Fase_03', 'Fase_04']

# 2. Omitindo o Início [:stop]
# O Python entende que deve começar do zero
print("\n2. As 3 primeiras fases [:3]:")
print(fases_testadas[:3])   
# Saída: ['Fase_01', 'Fase_02', 'Fase_03']

# 3. Omitindo o Fim [start:]
# Pega do índice escolhido até o final da lista
print("\n3. Da Fase 4 em diante [3:]:")
print(fases_testadas[3:])   
# Saída: ['Fase_04', 'Fase_05', 'Fase_06']

# 4. Usando o Passo [start:stop:step]
# Pega a lista inteira, mas pulando de 2 em 2
print("\n4. Fases ímpares (pulando de 2 em 2) [::2]:")
print(fases_testadas[::2])  
# Saída: ['Fase_01', 'Fase_03', 'Fase_05']

# 5. O Truque Ninja (Passo negativo)
# Inverte a lista lendo de trás para frente
print("\n5. Ordem inversa (últimos testes primeiro) [::-1]:")
print(fases_testadas[::-1]) 
# Saída: ['Fase_06', 'Fase_05', 'Fase_04', 'Fase_03', 'Fase_02', 'Fase_01']