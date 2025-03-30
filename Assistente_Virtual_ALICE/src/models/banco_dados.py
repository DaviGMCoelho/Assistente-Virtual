import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


import sqlite3

def conecta_banco_dados():
    conexao = sqlite3.connect(r'data\databases\alice_database.db') # Conecta a um banco de dados local
    terminal = conexao.cursor()

    return conexao, terminal


def cria_tabelas():
    conexao, terminal = conecta_banco_dados()
    terminal.execute('''
                        CREATE TABLE IF NOT EXISTS CONTATO(
                            ID_CONTATO INTEGER PRIMARY KEY,
                            NOME TEXT NOT NULL,
                            EMAIL TEXT NOT NULL,
                            CATEGORIA TEXT NOT NULL
                    );
                    ''')
    conexao.commit()
    conexao.close()


def insert_dados_emails(nome, email, categoria):
    conexao, terminal = conecta_banco_dados()
    terminal.execute(f'''
                     INSERT INTO CONTATO (NOME, EMAIL, CATEGORIA) VALUES ('{nome}', '{email}', '{categoria}');
                     ''')
    conexao.commit()
    conexao.close()


def verifica_banco_dados(tabela, coluna, dado):
    conexao, terminal = conecta_banco_dados()
    busca = terminal.execute(f'''
                             SELECT COUNT(*) FROM {tabela} WHERE {coluna} = '{dado}';
                             ''')
    resultado = busca.fetchone()[0]
    conexao.close()

    return resultado > 0


def apaga_dados_banco(tabela, id):
    conexao, terminal = conecta_banco_dados()
    query = f'''DELETE FROM {tabela} WHERE ID_CONTATO = ?;'''

    terminal.execute(query, (id,))
    conexao.commit()
    conexao.close()


def mostra_informacoes_tabela(tabela):
    conexao, terminal = conecta_banco_dados()
    informacoes_tabela = terminal.execute(f'''SELECT * FROM {tabela};''')
    resultado_bruto = informacoes_tabela.fetchall()

    resultado = [linha for linha in resultado_bruto]

    conexao.close()
    return resultado


if __name__ == '__main__':
    apaga_dados_banco('CONTATO', '1')
