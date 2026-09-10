"""Análise de Intersecção com Conjuntos (Sets)

Duas equipes de biólogos registraram as espécies de árvores encontradas em duas zonas diferentes da floresta.
zona_norte = {"Sumaúma", "Castanheira", "Seringueira", "Açaizeiro"}
zona_sul = {"Seringueira", "Açaizeiro", "Cupuaçuzeiro", "Andiroba"}

Usando operações de conjuntos (set), descubra e imprima:
As espécies que existem em ambas as zonas (Intersecção).

Todas as espécies únicas catalogadas no total, juntando as duas zonas (União).
As espécies que foram encontradas apenas na zona_norte (Diferença).
"""

zona_norte = {"Sumaúma", "Castanheira", "Seringueira", "Açaizeiro"}
zona_sul = {"Seringueira", "Açaizeiro", "Cupuaçuzeiro", "Andiroba"}

# 1. Intersecção (comum a ambos) - Usa o operador '&' ou método .intersection()
comuns = zona_norte & zona_sul
print(f"Espécies em ambas as zonas: {comuns}")

# 2. União (todas as espécies, sem duplicatas) - Usa o operador '|' ou .union()
todas_especies = zona_norte | zona_sul
print(f"Total de espécies biodiversas catalogadas: {todas_especies}")

# 3. Diferença (apenas na norte) - Usa o operador '-' ou .difference()
exclusivas_norte = zona_norte - zona_sul
print(f"Espécies exclusivas da Zona Norte: {exclusivas_norte}")
