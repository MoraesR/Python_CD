

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



