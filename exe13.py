""" Prevenindo Quebras com Try/Except
Um script de automação tenta ler um arquivo .csv gerado por um satélite, mas às vezes o satélite atrasa o envio e o arquivo não existe.
Escreva um bloco try...except.
No try, tente abrir um arquivo chamado dados_satelite_am.csv no modo de leitura e imprimir "Arquivo lido com sucesso".
No except, capture a exceção específica FileNotFoundError e imprima um aviso amigável: "Aviso: O arquivo do satélite ainda não está disponível."
"""