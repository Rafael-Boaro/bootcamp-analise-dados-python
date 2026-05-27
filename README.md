# 📊 Portefólio de Engenharia de Dados & IA: Python Bootcamp

Este repositório consolida as práticas de Análise de Dados, Engenharia de Dados (ETL), Machine Learning e Inteligência Artificial Generativa desenvolvidas durante o **Bootcamp de Análise de Dados com Python (Afya/DIO)**.

O objetivo do projeto é demonstrar a evolução de scripts básicos para arquiteturas robustas de software, aplicando regras de negócio, boas práticas de engenharia e integração com Modelos de Linguagem de Grande Escala (LLMs).

---

## 🛠️ Stack Tecnológica

* **Linguagens e Lógica:** Python 3
* **Manipulação de Dados:** Pandas, NumPy
* **Armazenamento:** SQLite (Relacional), JSON
* **Visualização:** Matplotlib
* **Machine Learning:** Scikit-Learn (Random Forest), Imbalanced-learn (SMOTE)
* **IA Generativa:** SDK `google-generativeai` (Gemini 1.5 Flash)
* **Boas Práticas:** Arquitetura modular, `try/except/finally`, e rastreabilidade via `logging`.

---

## 📂 Estrutura e Módulos do Projeto

O repositório está dividido em quatro módulos principais, refletindo uma esteira completa de desenvolvimento de sistemas orientados a dados:

### 1. Análise Exploratória (`inicio_teste/`)
* **Script:** `01_script_basico_exploratorio.py`
* **Descrição:** A fundação do projeto. Conecta a uma base SQLite local, insere dados estáticos, executa agrupamentos via Pandas e extrai resumos estatísticos (`.describe()`), exportando um relatório preliminar em formato JSON.

### 2. Pipeline ETL Corporativo (`pipeline_etl/`)
* **Script:** `02_pipeline_etl_avancado.py`
* **Descrição:** Refatoração do script básico para o padrão ETL (Extract, Transform, Load).
  * **Extract:** Extração idempotente e segura (`try/except`) da base de dados.
  * **Transform:** *Feature Engineering* e aplicação de regras de negócio (ex: cálculo de impostos e classificação de inventário).
  * **Load/Visualize:** Geração de gráficos analíticos automatizados exportados fisicamente (`relatorio_precos_v1.png`) para suporte à tomada de decisão.

### 3. Deteção de Anomalias em Produção (`Projeto_final/`)
* **Script:** `03_detector_anomalias_producao.py`
* **Descrição:** Pipeline de *Machine Learning* focado na segurança de transações financeiras.
  * Implementa um modelo `RandomForestClassifier`.
  * Utiliza `SMOTE` para tratamento e balanceamento de dados de fraudes (que representam apenas 2% das amostras).
  * Inclui normalização de dados (`StandardScaler`) e gera relatórios de explicabilidade (Matriz de Confusão e *Classification Report*).

### 4. CodeMaster AI - Assistente Virtual(Feito com auxilio de um agente de IA) (`agente-ia/`)
* **Script:** `assistente_virtual_producao.py`
* **Descrição:** Um Agente de IA Generativa atuando como arquiteto de software.
  * Integração direta com a API do Google Gemini.
  * Utiliza injeção de **Base de Conhecimento Privada** para contextualizar o LLM com regras de negócio e tabelas de preços, evitando alucinações.
  * Focado em suporte técnico e infraestrutura SaaS/Multi-Tenant.
