# Construinto um chatbot personalizado com GPT-4 e Linguagem Pyton
# Como não tenho assinatura do GPT-4 vou utilizar o GPT-3.5

# Import
import openai

# Chave
# Para o caso de upgrade para GPT-4
#openai.api_key='sua_chave_opi'  

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):
    
    # Obtém a resposta do modelo de linguagem
    response = openai.Completion.create(
        
        # Modelo usado
        # Outros modelos estão disponíveis em https://platform.openai.com/account/rate-limits
        engine = "text-davinci-003",
        
        # Texto inicial da conversa com o chatbot
        prompt = texto,
        
        # Comprimento da resposta gerada pelo modelo
        max_tokens = 150,
        
        # Quantas conclusões gerar para cada token
        n = 5,
        
        # O texto retornado não conterá a sequencia de parada
        stop = None,
        
        # Uma medida da aleatoriedade de um texto gerado pelo modelo. Seu valor está entre 0 e 1
        # Valores próximos a 1 significam que a saída é mais aleatória, enquanto valores próximos a zero 
        # significam que a saída é muito identificável
        temperature = 0.8
    )
    
    return response.choices[0].text.strip()

# Função principal do programa em Python
def main():
    print("\nBem-vindo ao GPT-3.5 Chatbot do Projeto 3 do Curso de Data Science Academy!")
    print("\nwww.datascienceacademy.com.br")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")
    
    # Loop
    while True:
        
        # Coleta a pergunta digitada pelo usuário
        user_message = input("\nVocê: ")
        
        # Se a mensagem for 'sair' finaliza o programa
        if user_message.lower() == "sair":
            break
        
        # Coloca a mensagem digitada pelo usuário na variável Python chamada gpt_prompt
        gpt_prompt = f"\nUsuário: {user_message}\nChatbot:"
        
        # Obtém a resposta do modelo executando a função gera_texto()
        chat_response = gera_texto(gpt_prompt)
        
        # Imprime a resposta do chatbot
        print(f"\nChatbot: {chat_response}")
        
# Execução do programa (bloco main) em Python
if __name__ == "__main__":
    main()
