

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
