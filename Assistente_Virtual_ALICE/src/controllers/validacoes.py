from datetime import datetime
#from commands.envia_email_commands import enviar_email_sem_anexo

ano_atual = datetime.now().year
data_atual = datetime.today()
nasceu = ''


def verifica_arquivo(arquivo, limite_arquivos):
    erros_arquivo = []
    
    if len(arquivo) > limite_arquivos:
        erros_arquivo.append(f'Limite de arquivos excedido, máximo de {limite_arquivos}.')

    return erros_arquivo


def verifica_senha_aplicativo(senha_aplicativo):
    erros_senha_aplicativo = []
    if len(senha_aplicativo) != 16:
        erros_senha_aplicativo.append(f'Tamanho de senha de app inválido')

    return erros_senha_aplicativo


def verifica_apelido(apelido):
    erros_apelido = []

    if apelido == '':
        erros_apelido.append('Digite um apelido para continuar.')

    else:
        if len(apelido) < 3 or len(apelido) > 15:
            erros_apelido.append('Apelido deve ter entre 3 a 15 caracteres.')
    return erros_apelido


def verifica_categoria(categoria):
    erros_categoria = []

    if categoria == '':
        erros_categoria.append('Digite uma categoria para continuar')
    else:
        if len(categoria) < 3 or len(categoria) > 30:
            erros_categoria.append('Categoria deve ter entre 3 a 30 caracteres')
    return erros_categoria


def verifica_email(email):
    erros_email = []

    if email == '':
        erros_email.append('Digite um email para continuar.')

    else:
        # Adicionar sistema de validação de email
        # Requisicao com smtplib?
        pass

    return erros_email


def verifica_senha(senha, confirmacao_senha):
    erros_senha = []

    if senha == '':
        erros_senha.append('Digite uma senha para continuar.')

    else:
        if len(senha) < 8:
            erros_senha.append('Senha precisa ter no mínimo 8 caracteres.')
        else:
            if senha != confirmacao_senha:
                erros_senha.append('As senhas não se coincidem')

    return erros_senha


def verifica_telefone(telefone):
    erros_telefone = []

    if telefone.isdigit():
        if len(telefone) < 11:
            erros_telefone.append('Telefone com quantidade de números inválidos.')
    else:
        if telefone == '':
            erros_telefone.append('Digite um número de telefone.')
        else:
            erros_telefone.append('Digite apenas números.')

    return erros_telefone


def verifica_data_nascimento(data):
    global data_atual, nasceu
    erros_data_nascimento = []
    data_nascimento = ''

    if not data:
        erros_data_nascimento.append('Coloque sua data de nascimento.')

    else:
        try:
            data_nascimento = datetime.strptime(data, '%d/%m/%Y').strftime('%d/%m/%Y')
        except ValueError:
            erros_data_nascimento.append('Data inválida.')
        

    return data_nascimento, erros_data_nascimento


def verifica_idade(data_nascimento):
    erros_idade = []
    if data_nascimento is None:
        dtime_data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        
        if ((data_atual - dtime_data_nascimento).days // 365) < 18:
            erros_idade.append('Você precisa ter 18 anos para usar esse programa.')
    return erros_idade
