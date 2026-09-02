from scipy.stats import ttest_ind

estatistica, p_valor = ttest_ind(pgnova, pgantiga)
print(f"P-value {p_valor: .4f}")

if p_valor < 0.05:
    print("rejeitado")
else:
    print("aceito")