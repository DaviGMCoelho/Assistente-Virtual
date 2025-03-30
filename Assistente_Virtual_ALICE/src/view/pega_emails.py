import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))


from customtkinter import *
from src.utils import tratar_texto_entrada
from src.controllers.pega_emails_controller import passa_email_controller, pega_contatos_cadastrados, pega_selecionadas, apaga_contatos_selecionados


def adicionar_contatos(entrada_nome, entrada_email, entrada_categoria, frame_dados):
    erros = []
    
    nome = entrada_nome.get()
    email = entrada_email.get()
    categoria = entrada_categoria.get()

    nome_tratado = tratar_texto_entrada(nome).capitalize()
    email_tratado = tratar_texto_entrada(email)
    categoria_tratada = tratar_texto_entrada(categoria)

    erros += passa_email_controller(nome_tratado, email_tratado, categoria_tratada)
    
    if erros:
        exibe_mensagem(erros, 'Erros encontrados')
    else:
        atualiza_lista_contatos(frame_dados)


def atualiza_lista_contatos(frame_dados):
    for elemento in frame_dados.winfo_children():
        elemento.destroy()
    carrega_informacoes_tela(frame_dados)


def carrega_informacoes_tela(frame_dados):
    contatos = pega_contatos_cadastrados()
    checkboxes = {}

    for contato in contatos:
        status = IntVar() # Guarda valor 0/1, saber status da checkbox
        checkbox = CTkCheckBox(frame_dados, text=contato, variable=status)
        checkbox.pack(anchor='w', padx=10, pady=2)
        checkboxes[contato] = status

    return checkboxes


def aviso_acao(mensagem, funcao, checkboxes):
    TAMANHO_BUTTON = 25
    ESPACO_BUTTON = 55

    confirmacao = CTkToplevel()
    confirmacao.grab_set()
    confirmacao.title('Aviso')
    confirmacao.geometry('325x85')
    
    aviso = CTkLabel(confirmacao, text=mensagem, font=('Arial', 15, 'bold'))
    aviso.pack(padx=10, pady=5)

    frame_botoes = CTkFrame(confirmacao)
    frame_botoes.pack()
    
    botao_cancelar = CTkButton(frame_botoes, text='Cancelar', font=('Arial', 15, 'bold'), height=TAMANHO_BUTTON, width=ESPACO_BUTTON, command=confirmacao.destroy)
    botao_cancelar.grid(row=0, column=0, pady=5, padx=5)

    botao_confirmar = CTkButton(
        frame_botoes, 
        text='Confirmar', 
        font=('Arial', 15, 'bold'), 
        height=TAMANHO_BUTTON, 
        width=ESPACO_BUTTON, 
        command=lambda: [funcao(checkboxes), confirmacao.destroy]
        )
    botao_confirmar.grid(row=0, column=1, pady=5, padx=5)


def remover_contatos(frame, checkboxes, funcao):
    funcao(checkboxes)
    novo_checkboxes = carrega_informacoes_tela(frame)
    checkboxes.clear()
    checkboxes.update(novo_checkboxes)


def verifica_selecionadas(checkboxes, funcao, frame_dados):
    selecionadas = pega_selecionadas(checkboxes)
    if len(selecionadas) > 0:
        aviso_acao('Deseja finalizar a ação?', lambda: remover_contatos(frame_dados, checkboxes, funcao))
    else:
        exibe_mensagem('Marque pelo menos uma opcao.', 'Aviso')


def exibe_mensagem(mensagem, titulo):
    janela_erros = CTkToplevel()
    janela_erros.grab_set() # Trava na janela_erros, não deixa mecher na janela principal sem tirar essa
    janela_erros.title(titulo)
    janela_erros.geometry('365x150')
    janela_erros.resizable(False, False)

    frame_mensagens = CTkFrame(janela_erros, width=360, height=90)
    frame_mensagens.pack(padx=10, pady=10)
    frame_mensagens.pack_propagate(False) # Tira o redimensionamento automático do frame

    if type(mensagem) == list:
        for frase in mensagem:
            texto = CTkLabel(frame_mensagens, text=frase, font=('Arial', 15, 'bold'))
            texto.pack(anchor='s')
    else:
        texto = CTkLabel(frame_mensagens, text=mensagem, font=('Arial', 15, 'bold'))
        texto.pack(anchor='s')

    botao_fechar = CTkButton(janela_erros, text='Entendi', command=janela_erros.destroy)
    botao_fechar.pack()

    janela_erros.mainloop()


def tela_cadastro_email():
    TAMANHO_BUTTON = 25
    ESPACO_BUTTON = 55
    ESPACO_ENTRY = 345
    TAMANHO_ENTRY = 35

    janela = CTk()
    janela.title('Destinatários')
    janela.geometry('390x465')
    janela.config(bg='#09112e')
    janela.resizable(False, False)

    frame_botoes = CTkFrame(janela, bg_color='#09112e', fg_color='#09112e')
    frame_botoes.grid(row=2, column=0)

    frame_barra_entrada = CTkFrame(janela, bg_color='#09112e')
    frame_barra_entrada.grid(row=1, column=0, padx=10, pady=10)

    titulo_lista = CTkLabel(janela, text='Destinatários', text_color='white', font=('Arial', 25, 'bold'), bg_color='#09112e')
    titulo_lista.grid(row=0, column=0, pady=10, sticky='s')

    espaco_nome = CTkEntry(
        frame_barra_entrada, 
        placeholder_text='Escreva aqui o nome...', 
        width=ESPACO_ENTRY, height=TAMANHO_ENTRY, fg_color='white', 
        placeholder_text_color='gray', 
        text_color='black', 
        bg_color='#09112e'
        )
    espaco_nome.grid(row=0, column=0, padx=(0, 5))

    espaco_email = CTkEntry(
        frame_barra_entrada, 
        placeholder_text='Escreva aqui o email...', 
        width=ESPACO_ENTRY, height=TAMANHO_ENTRY, 
        fg_color='white',
        placeholder_text_color='gray', 
        text_color='black', 
        bg_color='#09112e'
        )
    espaco_email.grid(row=1, column=0, padx=(0, 5))

    espaco_categoria = CTkEntry(
        frame_barra_entrada, 
        placeholder_text='Relação com essa pessoa: Trabalho, amigo, família', 
        width=ESPACO_ENTRY, height=TAMANHO_ENTRY, 
        fg_color='white',
        placeholder_text_color='gray', 
        text_color='black', 
        bg_color='#09112e'
        )
    espaco_categoria.grid(row=3, column=0, padx=(0,5))

    frame_dados = CTkScrollableFrame(janela, width=350, height=50)
    frame_dados.grid(row=3, column=0, pady=10, padx=10, sticky='nw')

    checkboxes = carrega_informacoes_tela(frame_dados)

    botao_adicionar = CTkButton(
        frame_botoes, 
        text='Adicionar', 
        height=TAMANHO_BUTTON, 
        width=ESPACO_BUTTON,
        command=lambda: adicionar_contatos(espaco_nome, espaco_email, espaco_categoria, frame_dados)
        )
    botao_adicionar.grid(row=0, column=1, pady=5, padx=5)

    botao_remover = CTkButton(
        frame_botoes, 
        text='Remover', 
        height=TAMANHO_BUTTON, 
        width=ESPACO_BUTTON, 
        command=lambda: [verifica_selecionadas(checkboxes, apaga_contatos_selecionados, frame_dados)]
        )
    
    botao_remover.grid(row=0, column=2, pady=5, padx=5)

    botao_editar = CTkButton(
        frame_botoes, 
        text='Editar', 
        height=TAMANHO_BUTTON, 
        width=ESPACO_BUTTON)
    botao_editar.grid(row=0, column=3, pady=5, padx=5)

    janela.mainloop()


if __name__ == '__main__':
    tela_cadastro_email()
