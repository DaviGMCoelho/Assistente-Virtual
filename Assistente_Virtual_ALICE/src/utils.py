import pyttsx3
from datetime import datetime
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import Tk, Label
import speech_recognition as sr
from customtkinter import *
import json

ARQUIVO_DADOS_USUARIO = r'data\databases\users\user.json'
voz = pyttsx3.init()
microfone = sr.Recognizer()


def carrega_todas_informacoes_usuario():
    global ARQUIVO_DADOS_USUARIO

    with open(ARQUIVO_DADOS_USUARIO, 'r') as arquivo:
        informacoes = json.load(arquivo)

    return informacoes


def carrega_informacoes_selecionadas_usuario(*dados):
    global ARQUIVO_DADOS_USUARIO
    informacoes = {}

    with open(ARQUIVO_DADOS_USUARIO, 'r') as arquivo:
        arquivo_json = json.load(arquivo)
    dados_usuario = arquivo_json[0]

    for dado in dados:
        for chave, valor in dados_usuario.items():
            if chave == dado:
                informacoes[chave] = valor

    return informacoes


def tratar_texto_entrada(texto):
    return texto.strip()


def captura_voz():
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source, None)
            try:
                frase = microfone.recognize_google(audio, language='pt-br').lower()
                return frase
            except sr.UnknownValueError:
                print('Não consegui te escutar')
            except Exception as error:
                print(f'Erro: {error}')


def data_hora():
    hoje = datetime.now()
    return hoje


def speak(frase):
    voz.say(frase)
    voz.runAndWait()


def escolher_arquivo(titulo):

    def drop(event):
        caminho = event.data
        arquivos.append(caminho)


    arquivos = []
    root = TkinterDnD.Tk()
    root.geometry('325x100')
    root.title(titulo)
    label = Label(root, text="Arraste e solte aqui, feche quando terminar!", bg="lightblue", width=40, height=5)
    label.pack(pady=20)
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)
    root.mainloop()
    
    return arquivos

if __name__ == '__main__':
    print(carrega_todas_informacoes_usuario())
    print(carrega_informacoes_selecionadas_usuario('email', 'senha_aplicativo'))
