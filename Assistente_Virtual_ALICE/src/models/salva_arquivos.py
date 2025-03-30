import os

def salva_arquivo_conversor(arquivo_convertido, informacao, nome_arquivo):
    if not os.path.exists(fr'output\texts\historico_conversor'):
        os.mkdir(fr'output\texts\historico_conversor')

    with open(fr'output\texts\historico_conversor\{nome_arquivo}\{nome_arquivo}.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(informacao)
    print('passei salva arquivo')