import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.controllers.validacoes import verifica_email, verifica_apelido, verifica_categoria
from src.models.banco_dados import insert_dados_emails, verifica_banco_dados, mostra_informacoes_tabela, apaga_dados_banco

# Ver se já existe no banco de dados

def passa_email_controller(nome, email, categoria):
    erros = []

    if verifica_email_existente(email):
        erros.append('Contato já cadastrado no sistema.')
        return erros

    erros += verifica_apelido(nome)
    erros += verifica_email(email)
    erros += verifica_categoria(categoria)
    if erros:
        return erros 

    insert_dados_emails(nome, email, categoria)
    return erros


def pega_selecionadas(checkboxes):
    return [texto for texto, status in checkboxes.items() if status.get() == 1]


def apaga_contatos_selecionados(checkboxes):
    for checkbox in checkboxes:
        id_contato = checkbox[0]
        apaga_dados_banco('CONTATO', id_contato)


def verifica_email_existente(dado):
    return verifica_banco_dados('CONTATO', 'EMAIL', dado)


def pega_contatos_cadastrados():
    return mostra_informacoes_tabela('CONTATO')


if __name__ == '__main__':
    print(pega_contatos_cadastrados())