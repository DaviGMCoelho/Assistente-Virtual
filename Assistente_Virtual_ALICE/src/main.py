import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import speech_recognition as sr
from nltk.tokenize import word_tokenize
from src.controllers.gerencia_comandos import comandos, carregar_comandos
from utils import speak, data_hora
import os
from src.view.cadastro_usuario import cadastro_usuario
import json

microfone = sr.Recognizer()

def tempo_agora():
    tempo = data_hora()
    hora = int(tempo.hour)
    if hora >= 5 and hora <= 11:
        saudacao = 'bom dia'
    elif hora >= 12 and hora <= 18:
        saudacao = 'boa tarde'
    else:
        saudacao = 'boa noite'
    return saudacao


def tratamento_frase(palavras):
    artigos = ['o','a','os','as']
    palavras_filtradas = [palavra for palavra in palavras if palavra not in artigos]
    return " ".join(palavras_filtradas)


def Assistente():
    arquivo_json = carregar_comandos()
    lista_iniciar = ['alice', 'iniciar assistente', 'iniciar']
    lista_fechar = ['desligar assistente', 'obrigado', 'tchau', 'adeus', 'até mais', 'brigado', 'obrigada', 'brigada']

    speak('Para iniciar, chame pelo meu nome ou diga "iniciar assistente" ou somente "Iniciar"!')
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None, 5)
            try:
                frase = microfone.recognize_google(audio, language='pt-br').lower()
                if any(palavra in frase for palavra in lista_iniciar):
                    print('ouvindo')
                    saudacao = tempo_agora()
                    speak(f'{saudacao}!, com o que posso te ajudar?')

                    assistente_funcionando = True
                    while assistente_funcionando:
                        with sr.Microphone() as source:
                            microfone.adjust_for_ambient_noise(source)
                            audio = microfone.listen(source, None)
                            try:
                                frase = microfone.recognize_google(audio, language='pt-br').lower()
                                palavras = word_tokenize(frase)
                                frase = tratamento_frase(palavras)

                                print('Usuario:', frase)
                                comandos(frase, arquivo_json)

                                if any(palavra in frase for palavra in lista_fechar):
                                    speak('Até mais! Fico feliz em ajudar!')
                                    assistente_funcionando = False

                            except sr.UnknownValueError:
                                print('Não consigo te escutar')
                            except Exception as error:
                                print(f'Erro: {error}')

            except sr.UnknownValueError:
                # Ignorar enquanto não estiver falando nada
                pass
            except Exception as error:
                print(f'Erro: {error}')

if os.path.exists(r'data\databases\users\user.json'):
    with open(r'data\databases\users\user.json', 'r') as arquivo:
        dados_usuario = json.load(arquivo)
    nome = dados_usuario[0]['nome']
    speak(f'Bem vindo de volta, {nome}!')
    Assistente()

else:
    cadastro_usuario()
    if os.path.exists(r'data\databases\users\user.json'):
        speak('Seja bem vindo!')
        Assistente()

