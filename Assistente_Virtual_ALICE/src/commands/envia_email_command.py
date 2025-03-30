import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import smtplib # Usada para realizar a conexão com o servidor
from email.mime.multipart import MIMEMultipart # Criar uma mensagem com textos e anexos
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from src.utils import carrega_informacoes_selecionadas_usuario


def enviar_email_sem_anexo(destinatario, assunto, mensagem):
    dados_usuario = carrega_informacoes_selecionadas_usuario('email', 'senha_aplicativo')
    email_usuario = dados_usuario['email']
    senha_aplicativo = dados_usuario['senha_aplicativo']

    smtp_server = 'smtp.gmail.com' # Define o server da comunicação smtp
    smtp_port = 587 # Porta padrão pra conexões tls/starttls
    remetente = email_usuario
    senha_aplicativo = senha_aplicativo

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(mensagem, 'plain')) # Adciona no corpo do email ( adiciona a mensagem ( mensagem, texto normal) )

    try:
        # conecta ao servidor SMTP para enviar o email
        server = smtplib.SMTP(smtp_server, smtp_port) # Tenta conectar ao servidor smtp
        server.starttls() # Usa TLS para segurança
        server.login(remetente, senha_aplicativo) # Entra no servidor

        server.sendmail(remetente, destinatario, msg.as_string())
        print('email enviado com sucesso')

    except Exception as error:
        print('Erro ao enviar o Email:', error)

    finally:
        server.quit() # Termina a conexão com o servidor


def enviar_email_com_anexo(destinatario, assunto, mensagem, anexos):
    dados_usuario = carrega_informacoes_selecionadas_usuario('email', 'senha_aplicativo')
    email_usuario = dados_usuario['email']
    senha_aplicativo = dados_usuario['senha_aplicativo']

    smtp_server = 'smtp.gmail.com' # Define o server da comunicação smtp
    smtp_port = 587 # Porta padrão pra conexões tls/starttls
    remetente = email_usuario
    senha_aplicativo = senha_aplicativo

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto


    msg.attach(MIMEText(mensagem, 'plain')) # Adciona no corpo do email ( adiciona a mensagem ( mensagem, texto normal) )
    
    try:
        if len(anexos) > 1:
            for arquivo in anexos:
                try:
                    nome_arquivo = os.path.basename(arquivo)
                    with open(arquivo, 'rb') as anexo: # Abre o arquivo para leitura em formato binário
                        part = MIMEApplication(anexo.read(), Name=nome_arquivo) # Anexo vira um objeto MIME aplication, podendo ser enviado e lido independente da extensão
                        #                                               ^ Coloca nome do arquivo como metadado
                    #                                                v Exibido com nome de:
                    part['Content-Disposition'] = f'attachment; filename="{nome_arquivo}"'
                    #        Cabeçalho                 ^ Diz que é um anexo
                    msg.attach(part)
                except Exception as e:
                    return f'Falha ao enviar arquivos: {e}'
        else:
            try:
                arquivo = anexos[0]
                nome_arquivo = os.path.basename(arquivo)
                with open(arquivo, 'rb') as anexo:
                    part = MIMEApplication(anexo.read(), Name=nome_arquivo)
                    
                part['Content-Disposition'] = f'attachement/ filename="{nome_arquivo}"'
                
                msg.attach(part)
            except Exception as e:
                return f'Falha ao enviar arquivos: {e}'

    except Exception as e:
        print(e)

    try:
        # conecta ao servidor SMTP para enviar o email
        server = smtplib.SMTP(smtp_server, smtp_port) # Tenta conectar ao servidor smtp
        server.starttls() # Usa TLS para segurança
        server.login(remetente, senha_aplicativo) # Entra no servidor

        server.sendmail(remetente, destinatario, msg.as_string())
        print('email enviado com sucesso')

    except Exception as error:
        print('Erro ao enviar o Email:', error)

    finally:
        server.quit() # Termina a conexão com o servidor
    