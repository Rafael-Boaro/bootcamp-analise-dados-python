# CodeMaster AI - Arquiteto de Software Virtual

Agente de IA Generativa focado em suporte técnico e arquitetural para desenvolvedores. Ele atua como um engenheiro de software parceiro, injetando contexto de infraestrutura e regras de negócio para solucionar problemas de código e plataformas Multi-Tenant.

## O Que é o CodeMaster AI?

O CodeMaster AI não gera apenas blocos de código genéricos. Ele é contextualizado com uma **Base de Conhecimento Privada** sobre os serviços, precificação e arquitetura técnica da plataforma na qual está inserido, garantindo respostas exatas e alinhadas ao modelo de negócio.

**O que o CodeMaster faz:**
- Explica arquiteturas e integrações de forma técnica e direta.
- Utiliza o contexto (Base de Conhecimento) para não alucinar informações de preços ou regras.
- Sugere melhorias arquiteturais visando Clean Code.

**O que o CodeMaster NÃO faz:**
- Não fornece dados inventados sobre a plataforma.
- Não foge do escopo de engenharia de software e suporte do produto.

## Arquitetura

O projeto foi construído utilizando a API da Google (`google-generativeai`) e arquitetura modular, permitindo fácil integração com Webhooks.

`Usuário` ➔ `Script Python` ➔ `Injeção de Base de Conhecimento (Contexto)` ➔ `Gemini LLM` ➔ `Resposta Técnica`
