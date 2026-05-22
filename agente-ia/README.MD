# 🤖 CodeMaster AI - Arquiteto de Software Virtual

Agente de IA Generativa focado em suporte técnico e arquitetural para desenvolvedores. Ele atua como um engenheiro de software parceiro, injetando contexto de infraestrutura e regras de negócio para solucionar problemas de código e plataformas Multi-Tenant.

## 💡 O Que é o CodeMaster AI?

O CodeMaster AI não gera apenas blocos de código genéricos. Ele é contextualizado com uma **Base de Conhecimento Privada** sobre os serviços, precificação e arquitetura técnica da plataforma na qual está inserido, garantindo respostas exatas e alinhadas ao modelo de negócio.

**O que o CodeMaster faz:**
- ✅ Explica arquiteturas e integrações de forma técnica e direta.
- ✅ Utiliza o contexto (Base de Conhecimento) para não alucinar informações de preços ou regras.
- ✅ Sugere melhorias arquiteturais visando Clean Code.

**O que o CodeMaster NÃO faz:**
- ❌ Não fornece dados inventados sobre a plataforma.
- ❌ Não foge do escopo de engenharia de software e suporte do produto.

## 🏗️ Arquitetura

O projeto foi construído utilizando a API da Google (`google-generativeai`) e arquitetura modular, permitindo fácil integração com Webhooks.

`Usuário` ➔ `Script Python` ➔ `Injeção de Base de Conhecimento (Contexto)` ➔ `Gemini LLM` ➔ `Resposta Técnica`

## ⚙️ Como Executar

**1. Instalar Dependências**
```bash
pip install google-generativeai
```

**2. Configurar a Chave da API**
Exporte a sua chave do Google AI Studio no seu terminal:

```bash
# Windows
set GEMINI_API_KEY="sua_chave_aqui"

# Linux/Mac
export GEMINI_API_KEY="sua_chave_aqui"
```

**3. Rodar o Agente**
```bash
python assistente_virtual_producao.py
```

## 🎯 Exemplo de Uso

**Pergunta do Usuário:** "Quais são os planos disponíveis e o que o Plano Pro oferece?"

**Resposta do CodeMaster:** "A plataforma oferece dois planos principais. O Plano Basic custa R$ 49/mês e garante acesso padrão às APIs. Já o Plano Pro, por R$ 99/mês, inclui suporte avançado a Webhooks e automação via n8n."

## 📊 Métricas de Avaliação

| Métrica | Objetivo alcançado no teste |
| :--- | :--- |
| **Assertividade** | O modelo respondeu exatamente aos valores definidos na base de conhecimento injetada. |
| **Segurança** | Tratamento de erros (`try/except`) implementado para evitar crashes na queda da API. |
| **Rastreabilidade** | Uso da biblioteca `logging` para monitorar todas as interações e erros em tempo real. |