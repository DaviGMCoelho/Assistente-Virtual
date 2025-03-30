import json
import webbrowser
import os
import sys

# Adiciona Yui no sys.path                   | retorna pasta atual   |
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
#              |torna um caminho| Sobe uma pasta no diretório               ||
# | Permite adicionar a pasta onde o python procura módulos                   |

from src.utils import speak, data_hora
from src.commands.calculadora_command import calculadora
from src.commands.gerador_texto_command import chat_bot_llama3
#from src.commands.envia_email_commands import gerenciador_emails
from src.commands.criacao_command import criacao

agora = data_hora()

def carregar_comandos():
    with open(r'comandos.json', 'r') as arquivo:
        dados = json.load(arquivo)
        comandos = dados['comandos']

    return comandos


def comandos(frase, comandos):
    for comando in comandos:
        if any(identificador in frase for identificador in comando["identificador"]):
            nome = comando["nome"]
            if nome == 'abrir':
                for item in comando["itens"]:
                    for palavra_chave in item["palavra_chave"]:
                        if palavra_chave in frase:
                            if item.get('url'):
                                webbrowser.open(item['url'])
                                speak(item["speak"])
                            if item.get('path'):
                                os.startfile(item['path'])
                                speak(item["speak"])
            if nome == 'horario':
                speak(f'Agoras são {agora.hour} horas e {agora.minute} minutos!')
            if nome == 'data':
                speak(f'Hoje é dia {agora.day} do {agora.month} de {agora.year}')
            if nome == 'calculadora':
                speak(calculadora(frase))
            if nome == 'gerador de texto':
                chat_bot_llama3(frase)
            #if nome == 'enviar email':
                #speak(gerenciador_emails())
            if nome == "criar":
                for item in comando['itens']:
                    for palavra_chave in item['palavras_chave']:
                        if palavra_chave in frase:
                            nome = item['objeto']
                            speak(criacao(nome))
                            break
            # Estudar threading e implementar relogio e timer para assistente de estudos


if __name__ == "__main__":
    speak(comandos(' ', carregar_comandos()))
