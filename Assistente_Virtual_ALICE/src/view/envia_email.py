import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))


from customtkinter import *
from src.utils import speak, captura_voz, escolher_arquivo
from pega_emails import tela_cadastro_email


def redirecionamento_emails():
    janela = CTk()
    #janela.geometry('350x200')
    janela.title('Gerenciador de Emails')
    janela.state('zoomed')
    
    texto_principal = CTkLabel(janela, text='Deseja enviar emails em massa?', font=('Arial', 15, 'bold'))
    texto_principal.pack(padx=10, pady=10)

    frame_botoes = CTkFrame(janela)
    frame_botoes.pack(padx=10, pady=10)

    botao_confirma = CTkButton(frame_botoes, text='Sim')
    botao_confirma.grid(row=0, column=0, padx=5)

    botao_cancela = CTkButton(frame_botoes, text='Não')
    botao_cancela.grid(row=0, column=1, padx=5)


    janela.mainloop()


def gerenciador_ems():
    ...
    


    
    
if __name__ == '__main__':
    redirecionamento_emails()
    
    
    