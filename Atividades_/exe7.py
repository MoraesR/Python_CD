""" 
Processamento de Dados em CSV
Crie via código um arquivo chamado precipitacao_mensal.csv contendo um cabeçalho "Mes,Precipitacao_mm" e três linhas de dados (ex: "Janeiro,250", "Fevereiro,310", "Março,295").
Escreva um segundo bloco de código que abra esse arquivo .csv, leia as linhas usando csv.reader, pule o cabeçalho e calcule a soma total da precipitação registrada nesses três meses.
"""

dados_para_salvar = [
    ["Mes", "Precipitacao_mm"], # Cabeçalho
    ["Janeiro", 250],
    ["Fevereiro", 310],
    ["Marco", 295]
]

with open("precipitacao_mensal.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados_para_salvar)
soma_precipitacao = 0

with open("precipitacao_mensal.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    
    # Pula a primeira linha (o cabeçalho) para não dar erro ao somar textos
    next(leitor) 
    
    for linha in leitor:
        # linha[0] é o Mês, linha[1] é o valor numérico (que vem como texto)
        valor = int(linha[1]) 
        soma_precipitacao += valor

print(f"Soma total da precipitação no trimestre: {soma_precipitacao} mm")
