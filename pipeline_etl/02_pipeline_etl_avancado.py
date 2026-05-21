import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

# 1. Configuração de Rastreabilidade (Logging)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DB_NAME = 'dados_corporativos.db'

def configurar_banco_de_dados() -> None:
    """Cria a estrutura relacional e insere dados iniciais de forma idempotente."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            # Cria a tabela apenas se não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    ano_lancamento INTEGER NOT NULL
                )
            ''')
            
            # Verifica se a tabela está vazia antes de inserir (Idempotência)
            cursor.execute('SELECT COUNT(*) FROM produtos')
            if cursor.fetchone()[0] == 0:
                produtos_iniciais = [
                    ('Notebook Pro', 7500.00, 2024),
                    ('Monitor Ultrawide', 2300.00, 2023),
                    ('Teclado Mecânico', 450.00, 2022),
                    ('Mouse Wireless', 250.00, 2024)
                ]
                cursor.executemany('INSERT INTO produtos (nome, preco, ano_lancamento) VALUES (?, ?, ?)', produtos_iniciais)
                logging.info("Dados iniciais inseridos com sucesso.")
            else:
                logging.info("Banco de dados já populado. Pulando inserção.")
                
    except sqlite3.Error as e:
        logging.error(f"Erro crítico na infraestrutura de banco de dados: {e}")
        raise

def extrair_dados() -> pd.DataFrame:
    """Extrai os dados do banco SQLite e converte para um DataFrame Pandas."""
    logging.info("Iniciando extração de dados (Extract)...")
    try:
        with sqlite3.connect(DB_NAME) as conn:
            query = "SELECT * FROM produtos"
            df = pd.read_sql_query(query, conn)
            return df
    except Exception as e:
        logging.error(f"Falha na extração de dados: {e}")
        raise

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica regras de negócio e engenharia de features (Transform)."""
    logging.info("Aplicando regras de negócio e transformação (Transform)...")
    
    # Regra 1: Cálculo de preço com margem de imposto (ex: 15%)
    df['preco_com_imposto'] = df['preco'] * 1.15
    
    # Regra 2: Classificação de inventário baseada no ano
    df['status_inventario'] = ['Lançamento' if ano >= 2024 else 'Catálogo Base' for ano in df['ano_lancamento']]
    
    return df

def gerar_relatorio_visual(df: pd.DataFrame) -> None:
    """Gera visualizações gráficas e exporta o relatório físico (Load/Visualize)."""
    logging.info("Gerando dashboard analítico...")
    
    # Configuração visual do gráfico
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['nome'], df['preco_com_imposto'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    plt.title('Análise de Preços de Produtos (Com Impostos)', fontsize=14, weight='bold')
    plt.xlabel('Categoria de Produto', fontsize=12)
    plt.ylabel('Valor Unitário (R$)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Adicionando os valores exatos em cima de cada barra
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f'R$ {yval:.2f}', ha='center', va='bottom', fontsize=10)

    # Exportação segura do relatório
    caminho_arquivo = 'relatorio_precos_v1.png'
    plt.savefig(caminho_arquivo, dpi=300, bbox_inches='tight')
    logging.info(f"Relatório exportado com sucesso para: {os.path.abspath(caminho_arquivo)}")
    
    # Exibe o gráfico em ambiente de desenvolvimento
    plt.show()

def main():
    """Função orquestradora do pipeline ETL."""
    logging.info("--- Iniciando Pipeline de Dados ---")
    try:
        configurar_banco_de_dados()
        dados_brutos = extrair_dados()
        
        if dados_brutos.empty:
            logging.warning("Nenhum dado encontrado para processamento.")
            return

        dados_transformados = transformar_dados(dados_brutos)
        
        # Exibe um resumo estatístico profissional no terminal
        logging.info(f"\nResumo Estatístico do Portfólio:\n{dados_transformados[['preco', 'preco_com_imposto']].describe()}")
        
        gerar_relatorio_visual(dados_transformados)
        
    except Exception as e:
        logging.critical(f"O pipeline falhou de forma inesperada: {e}")
    finally:
        logging.info("--- Execução do Pipeline Finalizada ---")

# Ponto de entrada padrão em Python
if __name__ == "__main__":
    main()