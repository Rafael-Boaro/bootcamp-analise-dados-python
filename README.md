# 📊 Pipeline de ETL e Análise de Dados com Python

Este repositório consolida as práticas de engenharia de dados e análise exploratória desenvolvidas durante o **Bootcamp de Análise de Dados com Python (Afya/DIO)**. 

O objetivo deste projeto é demonstrar a evolução de um script simples de análise de dados para um **Pipeline ETL (Extract, Transform, Load)** estruturado, aplicando regras de negócio e boas práticas de engenharia de software.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3
* **Banco de Dados:** SQLite (Relacional)
* **Manipulação e Transformação:** Pandas, NumPy
* **Visualização de Dados:** Matplotlib
* **Boas Práticas:** Módulo `logging` para rastreabilidade e arquitetura modular.

---

## 📂 Estrutura do Repositório

O projeto está dividido em duas etapas que demonstram a evolução da arquitetura de código:

### 1. `01_script_basico_exploratorio.py`
* **Foco:** Análise Exploratória.
* **Descrição:** A fundação do projeto. Um script de linha única que conecta ao banco SQLite, insere dados iniciais e utiliza o Pandas para agrupar as informações e extrair médias matemáticas simples (`.describe()`).

### 2. `02_pipeline_etl_avancado.py`
* **Foco:** Engenharia de Dados (Arquitetura Enterprise).
* **Descrição:** O código foi refatorado para o padrão ETL corporativo.
  * **Extract:** Conexão segura (`try/except/finally`) e extração idempotente do banco relacional.
  * **Transform:** *Feature Engineering* implementada com Pandas para cálculo de regras de negócio (ex: aplicação de impostos e classificação por ano de lançamento).
  * **Load/Visualize:** Geração de gráficos analíticos automatizados com Matplotlib e exportação física de relatórios (`.png`) para suporte à tomada de decisão.

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/rafael-boaro/bootcamp-analise-dados-python.git](https://github.com/rafael-boaro/bootcamp-analise-dados-python.git)
   
2. Instale as dependências analíticas:

   ```bash
   pip install pandas matplotlib numpy

3. Execute o pipeline de produção:

   ```bash
   python 02_pipeline_etl_avancado.py

O terminal exibirá os logs de execução de cada etapa da extração e o relatório visual será gerado e salvo na raiz do projeto.
