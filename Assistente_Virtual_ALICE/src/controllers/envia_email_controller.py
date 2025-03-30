import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.commands.envia_email_command import enviar_email_sem_anexo, enviar_email_com_anexo
from src.utils import speak, captura_voz, escolher_arquivo

