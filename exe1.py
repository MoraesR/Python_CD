#Desafio da aula 1

#Exercício 1: Manipulação de Dados em Listas
#Você está estruturando uma base de dados com as principais cidades de coleta de dados no estado.

#Crie uma lista chamada municípios contendo: "Manaus", "Parintins", "Itacoatiara", "Tefé" e "Coari".
#Adicione "Manacapuru" ao final da lista.
#Remova a cidade de "Tefé" da lista.
#Ordene a lista em ordem alfabética e imprima o resultado.


munic = ["Manaus", "Parintins", "Tefé", "Coari"]
print(munic)

munic.append("Manacapuru")
print(munic)

munic.sort() #aqui eu vou ordenei em ordem alfabética

munic.remove("Tefé") #deletei a cidade de Tefé

print(munic)


#agora vou inserir utilizando o insert e escolhendo o local na lista
munic.insert(0, "Sao Gabriel")
print(munic)

munic.insert(3, "Iranduba")
print(munic)