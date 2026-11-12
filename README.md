# Portfolio de Engenharia de Dados e IA: Python Bootcamp

Pipeline completo de engenharia de dados, transformacao ETL corporativa, deteccao de fraudes com Machine Learning e agente inteligente com Google Gemini.

## Visao geral

Este repositorio consolida as praticas de Analise de Dados, Engenharia de Dados (ETL), Machine Learning e Inteligencia Artificial Generativa desenvolvidas durante o **Bootcamp de Analise de Dados com Python (Afya/DIO)**.

O objetivo do projeto e demonstrar a evolucao de scripts basicos de manipulacao de dados para arquiteturas modulares e escalaveis de software, aplicando regras de negocio, tratamento de erros, balanceamento de classes em cenarios criticos de fraude e integracao com Modelos de Linguagem de Grande Escala (LLMs).

## Stack Tecnologica

| Camada | Tecnologia | Finalidade |
|---|---|---|
| Linguagem Base | Python 3.10+ | Desenvolvimento de scripts e pipelines |
| Manipulacao de Dados | Pandas, NumPy | Transformacoes e agregacoes estatisticas |
| Armazenamento | SQLite, JSON | Persistencia relacional leve e intercambio de dados |
| Visualizacao de Dados | Matplotlib | Geracao automatizada de graficos analiticos |
| Machine Learning | Scikit-Learn | Treinamento de classificador Random Forest |
| Balanceamento de Classes | Imbalanced-learn (SMOTE) | Sintese de dados para lidar com classes raras de fraude |
| Inteligencia Artificial | Google Generative AI (Gemini 1.5 Flash) | Assistente de arquitetura com injecao de contexto |
| Observabilidade | Logging (modulo nativo) | Rastreabilidade e auditoria de execucao |

## Estrutura e Modulos do Projeto

O repositorio esta estruturado em quatro modulos progressivos:

### 1. Analise Exploratoria (`inicio_teste/`)
- **Script:** `01_script_basico_exploratorio.py`
- **Descricao:** Conexao com banco SQLite local, insercao controlada de dados, execucao de operacoes de agrupamento via Pandas e extracao de metricas estatisticas (`.describe()`), exportando um relatorio inicial em JSON.

### 2. Pipeline ETL Corporativo (`pipeline_etl/`)
- **Script:** `02_pipeline_etl_avancado.py`
- **Descricao:** Pipeline completo seguindo o padrao Extract, Transform, Load:
  - **Extract:** Conexao idempotente com base de dados SQLite protegida com `try/except/finally`.
  - **Transform:** Engenharia de atributos (*Feature Engineering*) com calculo de impostos e classificacao de estoque.
  - **Load/Visualize:** Exportacao automatizada de relatorio grafico (`relatorio_precos_v1.png`) para suporte a decisao gerencial.

### 3. Deteccao de Anomalias em Producao (`Projeto_final/`)
- **Script:** `03_detector_anomalias_producao.py`
- **Descricao:** Pipeline de Machine Learning para identificacao de fraudes financeiras:
  - Treinamento de modelo ensemble com `RandomForestClassifier`.
  - Tratamento de base desbalanceada (onde fraudes representavam apenas 2% do volume) utilizando tecnica `SMOTE`.
  - Normalizacao de atributos com `StandardScaler` e avaliacao com Matriz de Confusao e *Classification Report*.

### 4. CodeMaster AI - Assistente Virtual (`agente-ia/`)
- **Script:** `assistente_virtual_producao.py`
- **Descricao:** Agente de IA generativa consumindo a API oficial do Google Gemini:
  - Injecao de **Base de Conhecimento Privada** para ancoragem do modelo, prevenindo alucinacoes sobre regras contratuais e tabelas de precos.
  - Respostas tecnicas focadas em arquitetura de microsservicos e sistemas multi-tenant.

## Instalacao e Execucao

### Pre-requisitos
- Python 3.10 ou superior instalado.
- Chave de API do Google Gemini (necessaria apenas para o modulo 4).

### 1. Clonar e configurar ambiente virtual

```bash
git clone https://github.com/Rafael-Boaro/bootcamp-analise-dados-python.git
cd bootcamp-analise-dados-python

# Criar e ativar o ambiente virtual no Linux Mint
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias necessarias
pip install pandas numpy scikit-learn imbalanced-learn matplotlib google-generativeai
```

### 2. Executar os modulos

Execucao da Analise Exploratoria:
```bash
python3 inicio_teste/01_script_basico_exploratorio.py
```

Execucao do Pipeline ETL:
```bash
python3 pipeline_etl/02_pipeline_etl_avancado.py
```

Execucao do Detector de Anomalias e Fraudes:
```bash
python3 Projeto_final/03_detector_anomalias_producao.py
```

Execucao do Agente de IA:
```bash
# Definir a chave de API do Gemini no terminal antes da execucao
export GEMINI_API_KEY="sua_chave_aqui"
python3 agente-ia/assistente_virtual_producao.py
```

## Decisoes tecnicas

- **Tratamento de dados desbalanceados com SMOTE:** Em analise de fraudes, a acuracia geral e uma metrica enganosa. O uso do SMOTE no modulo 3 garante que o modelo aprenda os padroes da classe minoritaria sem sofrer com overfitting severo.
- **Injecao de contexto (Grounding) no Agente:** Em vez de depender do conhecimento generico do LLM, o agente recebe explicitamente as diretrizes da empresa como prompt de sistema, garantindo conformidade operacional.
