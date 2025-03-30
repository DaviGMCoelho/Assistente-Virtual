import json

CAMINHO_ARQUIVO_USUARIO = r'data\databases\users\user.json'

def salva_usuario(usuario):
    global CAMINHO_ARQUIVO_USUARIO
    
    try:
        with open(CAMINHO_ARQUIVO_USUARIO, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    except json.JSONDecodeError:
        dados = []
    
    dados.append(usuario)

    with open(CAMINHO_ARQUIVO_USUARIO, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
