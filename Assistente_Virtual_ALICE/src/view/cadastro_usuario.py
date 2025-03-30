import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from customtkinter import *
from PIL import Image
import locale
from datetime import datetime

from src.utils import tratar_texto_entrada
from src.controllers.cadastro_usuario_controller import registra_usuario

locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")
ano_atual = datetime.now().year
data_atual = datetime.today()
lista_dia = [str(dia) for dia in range(1, 32)]
lista_mes = [str(mes) for mes in range(1, 13)]
lista_ano = [str(ano) for ano in range(1950, ano_atual + 1)]
erros = []


def pega_dados(frame_mensagem, espaco_nome, espaco_email, espaco_telefone, espaco_senha, espaco_confirma_senha, \
               espaco_dia_nascimento, espaco_mes_nascimento, espaco_ano_nascimento, espaco_senha_aplicativo):
    global erros
    nome = espaco_nome.get()
    email = espaco_email.get()
    telefone = espaco_telefone.get()
    senha = espaco_senha.get()
    confirma_senha = espaco_confirma_senha.get()
    dia_nascimento = espaco_dia_nascimento.get(),
    mes_nascimento = espaco_mes_nascimento.get(),
    ano_nascimento =  espaco_ano_nascimento.get(),
    senha_aplicativo = espaco_senha_aplicativo.get()

    dados_usuario_validar = {
        'nome': tratar_texto_entrada(nome),
        'email': tratar_texto_entrada(email),
        'telefone': tratar_texto_entrada(telefone),
        'senha': senha,
        'confirma_senha': confirma_senha,
        'data_nascimento': f'{dia_nascimento[0]}/{mes_nascimento[0]}/{ano_nascimento[0]}',
        'senha_aplicativo': tratar_texto_entrada(senha_aplicativo)
    }

    print(dados_usuario_validar['data_nascimento'])
    
    erros = registra_usuario(dados_usuario_validar)
    exibe_mensagem(erros, frame_mensagem)


def exibe_mensagem(lista_erros, text_box):
    text_box.configure(state="normal")
    text_box.delete("0.0", "end")  # Remove qualquer erro exibido previamente
    if lista_erros:
        for erro in lista_erros:
            text_box.insert("0.0", f'{erro}\n')  # insert at line 0 character 0
        text_box.configure(state="disabled")
    else:
        text_box.insert("0.0", 'Cadastro realizado com sucesso!')
        text_box.configure(state="disabled")


def cadastro_usuario():
    global espaco_nome, espaco_email, espaco_telefone, espaco_dia_nascimento, espaco_mes_nascimento, espaco_ano_nascimento, espaco_senha, espaco_confirma_senha
    TAMANHO_ENTRY = 265

    janela_cadastro = CTk()

    janela_cadastro.title('Cadastro de Usuário')
    janela_cadastro.geometry('690x470')
    janela_cadastro.config(background='white')
    janela_cadastro.resizable(False, False)
    imagem = CTkImage(Image.open(r'src\view\assets\icons\assistente_ALICE.png'), size=(260, 470))

    # FRAMES E PARTES DA TELA PRINCIPAL DO PROGRAMA 
    frame_imagem = CTkFrame(janela_cadastro, width=260, height=470, bg_color='gray', fg_color='gray', corner_radius=100)
    frame_imagem.grid(row=0, column=0)

    frame_principal = CTkFrame(janela_cadastro, width=420, height=470, bg_color='white', fg_color='white')
    frame_principal.grid(row=0, column=1, padx=(10, 0))

    frame_mensagem = CTkTextbox(frame_principal, width=420, height=125, font=('Arial', 14, 'bold'), text_color='blue', fg_color='white')
    frame_mensagem.grid(row=1, column=0)
    frame_mensagem.configure(state="disabled")


    # --------------------------- Adicionando elementos FRAME PRINCIPAL ---------------------------------------------------------------------------------
    frame_informacoes_cadastro = CTkFrame(frame_principal, fg_color='white', bg_color='white')
    frame_informacoes_cadastro.grid(row=0, column=0)

    frame_informacoes_nascimento = CTkFrame(frame_informacoes_cadastro, fg_color='white', bg_color='white')
    frame_informacoes_nascimento.grid(row=4, column=1, padx=10)

    titulo_frame_principal = CTkLabel(frame_informacoes_cadastro, text='Cadastro de usuário', text_color='black', font=('Times New Roman', 25, 'bold'))
    titulo_frame_principal.grid(row=0, column=0, pady=5, columnspan=2, sticky='w')

    texto_espaco_nome = CTkLabel(frame_informacoes_cadastro, text='Apelido', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_nome.grid(row=1, column=0, pady=5, sticky='w')
    espaco_nome = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Como deseja ser chamado?', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_nome.grid(row=1, column=1)

    texto_espaco_email = CTkLabel(frame_informacoes_cadastro, text='Email', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_email.grid(row=2, column=0, pady=5, sticky='w')
    espaco_email = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Digite seu email', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_email.grid(row=2, column=1)

    texto_espaco_telefone = CTkLabel(frame_informacoes_cadastro, text='Telefone', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_telefone.grid(row=3, column=0, pady=5, sticky='w')
    espaco_telefone = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Digite seu telefone, ex: 15123456789', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_telefone.grid(row=3, column=1)

    texto_espaco_data_nascimento = CTkLabel(frame_informacoes_cadastro, text='Nascimento', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_data_nascimento.grid(row=4, column=0, pady=5, sticky='w')

    espaco_dia_nascimento = CTkComboBox(frame_informacoes_nascimento, values=lista_dia, width=85, state='readonly', fg_color='white', text_color='black')
    espaco_dia_nascimento.set('-- Dia --')
    espaco_dia_nascimento.grid(row=0, column=0)
    espaco_mes_nascimento = CTkComboBox(frame_informacoes_nascimento, values=lista_mes, width=95, state='readonly', fg_color='white', text_color='black')
    espaco_mes_nascimento.set('-- Mês --')
    espaco_mes_nascimento.grid(row=0, column=1)
    espaco_ano_nascimento = CTkComboBox(frame_informacoes_nascimento, values=lista_ano, width=85, state='readonly', fg_color='white', text_color='black')
    espaco_ano_nascimento.set('-- Ano --')
    espaco_ano_nascimento.grid(row=0, column=2)

    texto_espaco_senha = CTkLabel(frame_informacoes_cadastro, text='Senha', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_senha.grid(row=5, column=0, pady=5, sticky='w')
    espaco_senha = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Digite sua senha, mínimo de 8 caracteres', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_senha.grid(row=5, column=1)

    texto_espaco_confirma_senha = CTkLabel(frame_informacoes_cadastro, text='Confirmar Senha', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_confirma_senha.grid(row=6, column=0, pady=5, sticky='w')
    espaco_confirma_senha = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Digite sua senha novamente', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_confirma_senha.grid(row=6, column=1)
    
    texto_espaco_senha_aplicativo = CTkLabel(frame_informacoes_cadastro, text='Senha App Google', text_color='black', font=('Arial', 15, 'bold'))
    texto_espaco_senha_aplicativo.grid(row=7, column=0, pady=5, sticky='w')
    espaco_senha_aplicativo = CTkEntry(frame_informacoes_cadastro, width=TAMANHO_ENTRY, placeholder_text='Digite sua senha de aplicativo', placeholder_text_color='black', fg_color='white', text_color='black')
    espaco_senha_aplicativo.grid(row=7, column=1)

    botao_salvar = CTkButton(frame_principal, text='Continuar', command=lambda: pega_dados(frame_mensagem, espaco_nome, espaco_email, 
                                                                                           espaco_telefone, espaco_senha, espaco_confirma_senha, 
                                                                                           espaco_dia_nascimento, espaco_mes_nascimento, espaco_ano_nascimento, espaco_senha_aplicativo))
    botao_salvar.grid(row=8, column=0, pady=5, padx=(0, 15), sticky='e')


    # --------------------------- Adicionando elementos FRAME IMAGEM ------------------------------------------------------------------------------------
    imagem = CTkLabel(frame_imagem, image=imagem, bg_color='gray', text=None)
    imagem.place(x=15, y=15)


    # --------------------------- FIM DO PROGRAMA -------------------------------------------------------------------------------------------------------
    janela_cadastro.mainloop()



if __name__ == '__main__':
    cadastro_usuario()
