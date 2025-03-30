import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
import time
from src.commands.envia_email_command import enviar_email_sem_anexo
from src.utils import speak, captura_voz, carrega_informacoes_selecionadas_usuario


def salva_arquivo(saida):
    if not os.path.exists(fr'output\texts\historico_gerador\{data_atual}'):
        os.mkdir(fr'output\texts\historico_gerador\{data_atual}')

    with open(fr'output\texts\historico_gerador\{data_atual}\{nome_arquivo}.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(saida)
        

def chat_bot_llama3(frase):
    destinatario = carrega_informacoes_selecionadas_usuario('email')
    
    speak('gerando texto... isso pode demorar um pouco')
    context = ''
    entrada = frase.lower()

    while True:
        nova_entrada = entrada
        saida = chain.invoke({"context": '', "question": nova_entrada}).replace('*', ' ').replace('-', ' ').replace('#', ' ')
        context += f"\nUsuário: {nova_entrada}\nAssistente: {saida}"
        speak('Arquivo criado')
        time.sleep(3)
        speak(saida)
        speak('Gostou? Posso salvar o arquivo? Fale "Sair" para fechar o gerador')
        resposta = captura_voz()

        if resposta == 'sair':
            return 'Cancelando operação'
        elif any(resposta in confirma for confirma in confirmacoes):
            salva_arquivo(saida)
            enviar_email_sem_anexo(destinatario, 'Gerador de texto', context)
            context = ''
            return f'Documento já está no histórico de conversas com nome de {nome_arquivo} e enviado para seu email!'
        elif any(resposta in negacao for negacao in negacoes):
            speak('Irei refazer, um momento')
            continue


agora = datetime.now()
data_atual = agora.strftime('%d-%m-%Y')
hora_atual = f'{agora.hour}H{agora.minute}M'
nome_arquivo = f'arquivo-{hora_atual}'

template = '''Responda a questão abaixo:
Este é um histórico da nossa conversa: {context}
Pergunta: {question}
Resposta: 
'''

model = OllamaLLM(model='llama3.1:8b')
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

confirmacoes = ['sim', 'perfeito', 'está bom', 'obrigado', 'tá bom', 'ótimo', 'pode salvar', 'salvar', 'salve']
negacoes = ['não', 'não gostei', 'refaça', 'não salve', 'faz outro', 'refaz', 'não salvar']

if __name__ == '__main__':
    print(chat_bot_llama3('me fale 3 ideias de projetos em python'))
    