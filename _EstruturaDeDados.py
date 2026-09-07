"""
Listas (list)

Tuplas (tuple)

Dicionários (dict)

Conjuntos (set)
"""

#. Listas
# Criando uma lista de alunos
alunos = ["Ana", "Carlos", "Beatriz", "João"]

# 1. Acessando elementos pelo índice (começa no 0)
print(alunos[0])  # Saída: Ana
print(alunos[-1]) # Saída: João (último elemento)

# 2. Adicionando novos elementos
alunos.append("Marcos")     # Adiciona ao final
alunos.insert(1, "Daniela") # Insere na posição de índice 1

# 3. Modificando elementos (mutabilidade)
alunos[0] = "Ana Clara"

# 4. Removendo elementos
alunos.remove("Carlos") # Remove pelo valor
ultimo = alunos.pop()   # Remove e retorna o último elemento ("Marcos")

# 5. Percorrendo a lista com um loop
for aluno in alunos:
    print(f"Estudante: {aluno}")

print("Tamanho da lista:", len(alunos))



#Tuplas

# Coordenadas geográficas de Manaus (Latitude, Longitude)
coordenadas_manaus = (-3.1190275, -60.0217314)

# 1. Acessando elementos
print("Latitude:", coordenadas_manaus[0])
print("Longitude:", coordenadas_manaus[1])

# 2. Tentativa de alteração (gera erro proposital)
# coordenadas_manaus[0] = -3.12  # TypeError: 'tuple' object does not support item assignment

# 3. Desempacotamento de valores (Unpacking)
lat, lon = coordenadas_manaus
print(f"Lat: {lat} | Lon: {lon}")

# 4. Tupla com um único elemento (exige vírgula no final!)
tupla_unitaria = ("valor único",)



#Dicionários 

# Ficha de cadastro de um sensor IoT
sensor = {
    "id": "SNS-001",
    "tipo": "Temperatura",
    "localizacao": "Laboratório 02",
    "temperatura_atual": 24.5,
    "ativo": True
}

# 1. Acessando valores através da chave
print(sensor["tipo"])  # Saída: Temperatura

# Forma segura com .get() (não gera erro caso a chave não exista)
print(sensor.get("bateria", "Chave não encontrada!"))

# 2. Adicionando ou atualizando campos
sensor["temperatura_atual"] = 26.1  # Atualiza valor existente
sensor["bateria"] = 98               # Cria uma nova chave

# 3. Removendo uma chave
del sensor["ativo"]

# 4. Iterando sobre o dicionário
for chave, valor in sensor.items():
    print(f"{chave.upper()}: {valor}")



#Conjuntos
# Lista com CPFs duplicados
cpfs_brutos = ["111", "222", "111", "333", "222", "444"]

# 1. Removendo duplicatas instantaneamente com set
cpfs_unicos = set(cpfs_brutos)
print("CPFs Únicos:", cpfs_unicos)  # Saída: {'111', '222', '333', '444'}

# 2. Operações de Conjuntos
turma_ia = {"Ana", "Carlos", "Marcos", "Beatriz"}
turma_jogos = {"Beatriz", "João", "Carlos", "Fernanda"}

# Interseção: Quem faz ambos os cursos?
alunos_ambos = turma_ia.intersection(turma_jogos)
print("Em ambos os cursos:", alunos_ambos)  # {'Carlos', 'Beatriz'}

# Diferença: Quem faz apenas IA?
apenas_ia = turma_ia.difference(turma_jogos)
print("Apenas no curso de IA:", apenas_ia)  # {'Ana', 'Marcos'}



