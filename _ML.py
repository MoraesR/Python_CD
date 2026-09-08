"""
Projeto: Preditor de Atraso Logístico
Objetivo: Classificar se uma entrega atrasará (1) ou não (0) com base em variáveis da rota, clima e veículo.
Ambiente: Python 3.10+ com Pandas, NumPy e Scikit-Learn.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ==============================================================================
# 1. GERAÇÃO DE DADOS SINTÉTICOS (Para testes locais/Colab)
# ==============================================================================
np.random.seed(42)
n_samples = 1200

distancias_km = np.random.uniform(5.0, 60.0, n_samples)
turnos = np.random.choice(["Manhã", "Tarde", "Noite"], n_samples, p=[0.4, 0.4, 0.2])
condicoes_clima = np.random.choice(["Limpo", "Chuva Leve", "Chuva Forte"], n_samples, p=[0.6, 0.25, 0.15])
tipos_veiculo = np.random.choice(["Moto", "Van", "Caminhão Leve"], n_samples, p=[0.5, 0.35, 0.15])
paradas_intermediarias = np.random.poisson(lam=3, size=n_samples)

# Probabilidade lógica de atraso baseada nos fatores
risco_atraso = (
    0.02 * distancias_km
    + 0.15 * paradas_intermediarias
    + np.where(condicoes_clima == "Chuva Forte", 1.8, 0.0)
    + np.where(condicoes_clima == "Chuva Leve", 0.6, 0.0)
    + np.where(turnos == "Tarde", 0.5, 0.0)
    + np.random.normal(0, 0.8, n_samples)
)

# Target: 1 se atrasou, 0 se entregou no prazo
atrasou = (risco_atraso > np.percentile(risco_atraso, 65)).astype(int)

df = pd.DataFrame({
    "distancia_km": distancias_km,
    "paradas": paradas_intermediarias,
    "turno": turnos,
    "clima": condicoes_clima,
    "tipo_veiculo": tipos_veiculo,
    "atrasou": atrasou
})

print("--- Amostra dos Dados ---")
print(df.head())
print(f"\nDistribuição das Classes:\n{df['atrasou'].value_counts(normalize=True).round(2)}")

# ==============================================================================
# 2. DEFINIÇÃO DE FEATURES E SEPARAÇÃO DE AMOSTRAS
# ==============================================================================
features_numericas = ["distancia_km", "paradas"]
features_categoricas = ["turno", "clima", "tipo_veiculo"]

X = df[features_numericas + features_categoricas]
y = df["atrasou"]

# Separação estratificada (mantém proporção de 0s e 1s em treino e teste)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# ==============================================================================
# 3. PIPELINE DE PRÉ-PROCESSAMENTO
# ==============================================================================
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), features_numericas),
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), features_categoricas)
    ]
)

# ==============================================================================
# 4. CONSTRUÇÃO DOS MODELOS (Baseline vs Random Forest)
# ==============================================================================
# Modelo 1: Baseline linear
pipeline_lr = Pipeline(steps=[
    ("prep", preprocessor),
    ("clf", LogisticRegression(random_state=42))
])

# Modelo 2: Classificador não-linear baseado em árvores
pipeline_rf = Pipeline(steps=[
    ("prep", preprocessor),
    ("clf", RandomForestClassifier(n_estimators=120, max_depth=6, random_state=42))
])

# Treinamento
pipeline_lr.fit(X_train, y_train)
pipeline_rf.fit(X_train, y_train)

# ==============================================================================
# 5. AVALIAÇÃO DOS MODELOS
# ==============================================================================
def avaliar_modelo(nome, pipeline, X_val, y_val):
    preds = pipeline.predict(X_val)
    probas = pipeline.predict_proba(X_val)[:, 1]
    
    print(f"\n==================== {nome} ====================")
    print("Relatório de Classificação:")
    print(classification_report(y_val, preds, target_names=["No Prazo", "Atrasado"]))
    print(f"ROC-AUC Score: {roc_auc_score(y_val, probas):.4f}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_val, preds))

avaliar_modelo("Regressão Logística (Baseline)", pipeline_lr, X_test, y_test)
avaliar_modelo("Random Forest", pipeline_rf, X_test, y_test)

# ==============================================================================
# 6. INFERÊNCIA EM TEMPO REAL (Novos Dados)
# ==============================================================================
novo_cenario = pd.DataFrame([{
    "distancia_km": 42.5,
    "paradas": 5,
    "turno": "Tarde",
    "clima": "Chuva Forte",
    "tipo_veiculo": "Moto"
}])

prob_atraso = pipeline_rf.predict_proba(novo_cenario)[0][1]
classe_predita = pipeline_rf.predict(novo_cenario)[0]

print("\n--- Teste de Inferência de Produção ---")
print(novo_cenario.to_dict(orient="records")[0])
print(f"Predição: {'Atraso Provável' if classe_predita == 1 else 'Entrega no Prazo'}")
print(f"Probabilidade estimada de atraso: {prob_atraso * 100:.2f}%")