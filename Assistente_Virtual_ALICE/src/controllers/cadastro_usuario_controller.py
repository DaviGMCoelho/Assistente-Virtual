import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.controllers.validacoes import verifica_apelido, verifica_email, verifica_telefone, \
    verifica_data_nascimento, verifica_senha, verifica_idade, verifica_senha_aplicativo
from src.models.usuario import salva_usuario


def valida_cadastro(dados_usuario_validar):
    erros = []

    erros += verifica_apelido(dados_usuario_validar['nome'])
    erros += verifica_email(dados_usuario_validar['email'])
    erros += verifica_telefone(dados_usuario_validar['telefone'])
    data_nascimento, erros_data_nascimento = verifica_data_nascimento(dados_usuario_validar['data_nascimento'])
    erros += erros_data_nascimento
    erros += verifica_senha(dados_usuario_validar['senha'], dados_usuario_validar['confirma_senha'])
    erros += verifica_senha_aplicativo(dados_usuario_validar['senha_aplicativo'])

    if erros_data_nascimento is not None:
        erros += verifica_idade(dados_usuario_validar['data_nascimento'])

    return data_nascimento, erros


def registra_usuario(dados_usuario):
    data_nascimento, erros = valida_cadastro(dados_usuario)
    if erros:
        return erros
    dados_usuario['data_nascimento'] = data_nascimento
    del dados_usuario['confirma_senha']
    
    salva_usuario(dados_usuario)

