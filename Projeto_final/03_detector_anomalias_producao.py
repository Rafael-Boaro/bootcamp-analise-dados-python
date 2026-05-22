import os
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification

# 1. Configuração de Rastreabilidade
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

ARQUIVO_DADOS = 'transacoes_financeiras.csv'

def carregar_dados() -> pd.DataFrame:
    """Extrai os dados do CSV ou gera um dataset sintético caso não exista (Fallback)."""
    logging.info("Iniciando extração de dados...")
    if os.path.exists(ARQUIVO_DADOS):
        return pd.read_csv(ARQUIVO_DADOS)
    
    logging.warning("Arquivo CSV não encontrado. Gerando dataset sintético de anomalias (fraudes) para simulação.")
    # Gera 10.000 transações onde apenas 2% são anomalias (fraudes)
    X, y = make_classification(n_samples=10000, n_features=10, n_informative=5, 
                               n_classes=2, weights=[0.98, 0.02], random_state=42)
    
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(1, 11)])
    df['Class'] = y
    return df

def pre_processar_e_balancear(df: pd.DataFrame):
    """Aplica o Feature Scaling e o balanceamento de classes com SMOTE."""
    logging.info("Iniciando pré-processamento e balanceamento...")
    
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Divisão de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Padronização (Transform)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Balanceamento com SMOTE (Exigência da etapa 2 do desafio)
    smote = SMOTE(random_state=42)
    X_train_bal, y_train_bal = smote.fit_resample(X_train_scaled, y_train)
    
    logging.info(f"Distribuição original: {dict(y_train.value_counts())}")
    logging.info(f"Distribuição após SMOTE: {dict(y_train_bal.value_counts())}")
    
    return X_train_bal, X_test_scaled, y_train_bal, y_test

def treinar_e_avaliar_modelo(X_train, X_test, y_train, y_test) -> None:
    """Treina o modelo avançado e exibe as métricas de explicabilidade."""
    logging.info("Treinando modelo avançado (Random Forest)...")
    
    modelo = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    modelo.fit(X_train, y_train)
    
    logging.info("Gerando predições e avaliando métricas...")
    previsoes = modelo.predict(X_test)
    
    print("\n" + "="*50)
    print("MÉTRICAS DE AVALIAÇÃO - DETECÇÃO DE ANOMALIAS")
    print("="*50)
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, previsoes))
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, previsoes))
    print("="*50 + "\n")

def main():
    """Função orquestradora do pipeline de Machine Learning."""
    logging.info("--- Iniciando Pipeline de Detecção de Anomalias ---")
    try:
        dados_brutos = carregar_dados()
        
        X_train, X_test, y_train, y_test = pre_processar_e_balancear(dados_brutos)
        
        treinar_e_avaliar_modelo(X_train, X_test, y_train, y_test)
        
    except Exception as e:
        logging.critical(f"O pipeline falhou de forma inesperada: {e}")
    finally:
        logging.info("--- Execução do Pipeline Finalizada ---")

if __name__ == "__main__":
    main()