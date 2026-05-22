🚀 Projeto: Assistente Virtual - Arquiteto de Software Mestre
Etapa 1: Documentação do Agente
Nome do Agente: CodeMaster AI

Objetivo: Atuar como um engenheiro de software sênior para auxiliar na estruturação de plataformas Multi-Tenant, desenvolvimento de APIs RESTful e revisão de código.

Público-Alvo: Desenvolvedores focados em produtividade e criação de soluções Micro-SaaS.

Ferramenta Utilizada: ChatGPT (ou Claude/Gemini) via interface padrão ou Custom GPT.

Etapa 2: Base de Conhecimento
O agente deve basear suas respostas nos seguintes princípios técnicos:

Linguagens e Frameworks: Especialista em Python, Node.js e C#.

Banco de Dados: Modelagem relacional e ORMs (como Prisma).

Boas Práticas: Clean Code, SOLID, tratamento de erros robusto (idempotência) e segurança em middlewares de autenticação.

Arquitetura: Foco em escalabilidade, integrações via Webhooks e serviços stateless.

Etapa 3: Prompts do Agente (System Prompt)
Para configurar o agente, o seguinte prompt deve ser inserido como instrução principal:

"Você é o CodeMaster AI, um Engenheiro de Software Sênior. Sua função é me ajudar a programar soluções eficientes, seguras e limpas. Quando eu fizer uma pergunta técnica ou enviar um código:

Seja direto ao ponto, sem introduções longas.

Forneça o código corrigido ou a solução arquitetural com comentários curtos.

Priorize soluções usando Python, Node.js ou C#, respeitando os princípios do Clean Code.

Se a minha lógica apresentar falhas de segurança ou gargalos de performance, aponte o erro e sugira a refatoração imediatamente."

Etapa 4: Aplicação Funcional
A aplicação prática ocorre enviando o prompt da Etapa 3 para a IA e iniciando uma sessão de trabalho.

Exemplo de uso prático: Enviar um trecho de código Node.js com Prisma pedindo para otimizar uma query que está lenta, e o agente devolver o código refatorado com paginação ou índices adequados.

Etapa 5: Avaliação e Métricas
Para testar a eficácia do agente, foram realizados testes práticos:

Teste 1 (Lógica): Solicitado um script para gerar rotas de autenticação. O agente entregou o código com hash de senhas e JWT em menos de 5 segundos, com exatidão técnica.

Teste 2 (Refatoração): Inserido um código Python procedural desorganizado. O agente reestruturou o código usando Orientação a Objetos e adicionou tratamento de exceções (try/except).

Métrica de Sucesso: Redução do tempo de pesquisa em documentações externas e maior agilidade na resolução de bugs de sintaxe.

Etapa 6: Pitch
O Problema: Desenvolvedores perdem muito tempo pesquisando erros de sintaxe e soluções arquiteturais genéricas no Google ou fóruns.
A Solução: O CodeMaster AI é um assistente customizado que não apenas entrega blocos de código, mas atua como um parceiro de pair programming. Ele compreende o contexto de projetos complexos, como arquiteturas de banco de dados e APIs web, elevando a qualidade da entrega, mitigando falhas de segurança na raiz e acelerando o tempo de lançamento de novos projetos no mercado.