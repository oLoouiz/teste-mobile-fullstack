import os
from datetime import datetime

LOG_FILE = os.path.join('Save', 'log.txt')

def salvarLog(mensagem):
    if not os.path.exists('Save'):
        os.makedirs('Save')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensagem_completa = f"{timestamp} - {mensagem}\n"

    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(mensagem_completa)

salvarLog("Teste")