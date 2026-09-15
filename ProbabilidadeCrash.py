"""
Resolução Bayesiana de Bugs de QA
"""

def calcular_bayes(p_A, p_B, p_B_dado_A):
    """
    Calcula P(A|B) usando o Teorema de Bayes.
    """
    p_A_dado_B = (p_B_dado_A * p_A) / p_B
    return p_A_dado_B

# Definindo as probabilidades dadas pelo problema
prob_crash = 0.20                   # P(A)
prob_nivel2 = 0.40                  # P(B)
prob_nivel2_dado_crash = 0.75       # P(B|A)




# Executando a função
resultado = calcular_bayes(prob_crash, prob_nivel2, prob_nivel2_dado_crash)

print("--- Relatório de QA: Corpo-Seco ---")
print(f"Risco de Crash ao entrar no Nível 2: {resultado * 100:.1f}%")