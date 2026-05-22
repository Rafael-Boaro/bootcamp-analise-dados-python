import os
import logging
import google.generativeai as genai

# Configuração de Rastreabilidade
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AgenteAssistenteVirtual:
    """
    Etapa 1: Documentação do Agente
    Objetivo: Assistente técnico especializado em resolver problemas de integração e 
    fornecer informações sobre planos de uma plataforma Micro-SaaS.
    Público-alvo: Desenvolvedores e clientes da plataforma.
    """

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        
        # Etapa 3: Prompts do Agente (System Prompt)
        self.instrucao_sistema = (
            "És um Assistente Virtual técnico integrado a uma plataforma SaaS. "
            "O teu objetivo é ajudar utilizadores com dúvidas sobre APIs, configuração de webhooks "
            "e gestão de assinaturas. Sê direto, extremamente técnico, focado em exatidão e "
            "não dês informações fora da tua base de conhecimento."
        )
        
        # Etapa 2: Base de Conhecimento (Contexto Privado)
        self.base_conhecimento = (
            "INFORMAÇÕES DA PLATAFORMA:\n"
            "- Plano Basic: R$ 49/mês (Acesso padrão a APIs).\n"
            "- Plano Pro: R$ 99/mês (Suporte a Webhooks e automação via n8n).\n"
            "- Arquitetura: Plataforma construída em Node.js com Prisma ORM.\n"
            "- Suporte de Integração: Para recuperar perdas ou automatizar rotinas, utilize nós de IA integrados aos webhooks.\n"
        )
        
        # Etapa 4: Aplicação Funcional
        self.modelo = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=self.instrucao_sistema
        )
        self.chat = self.modelo.start_chat(history=[])

    def processar_interacao(self, mensagem_usuario: str) -> str:
        """Recebe a mensagem, injeta a base de conhecimento e retorna a resposta."""
        try:
            logging.info(f"Processando requisição de utilizador: '{mensagem_usuario}'")
            
            # Construção do Prompt final injetando a Base de Conhecimento
            prompt_contextualizado = (
                f"Usa a seguinte Base de Conhecimento Privada para responder:\n"
                f"{self.base_conhecimento}\n\n"
                f"Pergunta do Utilizador:\n{mensagem_usuario}"
            )
            
            resposta = self.chat.send_message(prompt_contextualizado)
            return resposta.text
        
        except Exception as e:
            logging.error(f"Falha de comunicação com a LLM: {e}")
            return "Erro interno de processamento. Tente novamente mais tarde."

def main():
    """Função orquestradora (Etapa 4: Aplicação Funcional e Etapa 5: Testes/Avaliação)."""
    logging.info("--- Iniciando Agente Assistente Virtual ---")
    
    # Substitua pela sua chave de API ou configure no ambiente
    API_KEY = os.getenv("GEMINI_API_KEY", "SUA_API_KEY_AQUI")
    
    if API_KEY == "SUA_API_KEY_AQUI":
        logging.warning("Modo de teste: A API Key não foi configurada. O modelo pode falhar na execução real.")
    
    agente = AgenteAssistenteVirtual(api_key=API_KEY)
    
    # Etapa 5: Avaliação e Métricas na Prática (Simulação de Interações)
    perguntas_teste = [
        "Quais são os planos disponíveis e o que o Plano Pro oferece?",
        "Qual a stack do back-end da plataforma?"
    ]
    
    print("\n" + "="*50)
    for pergunta in perguntas_teste:
        print(f"👤 Utilizador: {pergunta}")
        resposta = agente.processar_interacao(pergunta)
        print(f"🤖 Assistente:\n{resposta}\n" + "-"*50)

if __name__ == "__main__":
    main()