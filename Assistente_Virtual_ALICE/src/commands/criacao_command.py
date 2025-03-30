import os

DESKTOP_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')


def criacao(nome):
    global DESKTOP_PATH

    if nome == 'pasta':
        numero_pasta = 0
        nome_base = os.path.join(DESKTOP_PATH, 'Nova_Pasta')
        nome_pasta = nome_base

        while os.path.exists(nome_pasta):
            numero_pasta += 1
            nome_pasta = f'{nome_base}_({numero_pasta})'
        os.makedirs(nome_pasta)
        return 'Pasta criada!'
    
    if nome == 'python':
        numero_arquivo = 0
        nome_base = os.path.join(DESKTOP_PATH, 'Arquivo_Python')
        nome_arquivo = f'{nome_base}.py'

        while os.path.exists(nome_arquivo):
            numero_arquivo += 1
            nome_arquivo = f'{nome_base}_({numero_arquivo}).py'
        
        with open(nome_arquivo, 'x') as arquivo:
            return 'Arquivo Python criado!'