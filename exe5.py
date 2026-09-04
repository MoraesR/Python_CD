""" Interface de Automação (While Loop)
Crie um menu de terminal contínuo para um sistema de coleta de dados. 
O programa deve exibir as opções: 
1. Inserir nova medição 
2. Visualizar relatório 
3. Sair
O sistema deve usar um while para continuar rodando 
e pedindo a escolha do usuário. Só deve ser encerrado quando o usuário digitar 3.
"""



medicoes = []


while True:
    print("\n==================================")
    print("      SISTEMA DE COLETA DE DADOS   ")
    print("==================================")
    print("1. Inserir nova medição")
    print("2. Visualizar relatório")
    print("3. Sair")
    
    
    opcao = input("\nEscolha uma opção (1-3): ").strip()
    
    if opcao == '1':
        
        entrada = input("Digite o valor da medição: ")
        try:
            valor = float(entrada)
            medicoes.append(valor)
            print(f"Sucesso: Medição {valor} adicionada com sucesso!")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
            
    elif opcao == '2':
       
        print("\n--- RELATÓRIO DE MEDIÇÕES ---")
        if len(medicoes) == 0:
            print("Nenhuma medição registrada até o momento.")
        else:
            print(f"Total de medições registradas: {len(medicoes)}")
            print(f"Valores: {medicoes}")
           
            media = sum(medicoes) / len(medicoes)
            print(f"Média das medições: {media:.2f}")
            print(f"Maior valor: {max(medicoes)}")
            print(f"Menor valor: {min(medicoes)}")
            
    elif opcao == '3':
        
        print("\nEncerrando o sistema de coleta. Até logo!")
        break  
        
    else:
       
        print("\n[Aviso] Opção inválida! Escolha um número entre 1 e 3.")