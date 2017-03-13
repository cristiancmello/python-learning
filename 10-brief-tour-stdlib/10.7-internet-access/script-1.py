# Internet Access
# Há alguns módulos que proveem acesso à Internet e seus protocolos.

# Módulo 'smtplib'
# Fornece funções para processamento de email.
# Para funcionar, é preciso instalar um servidor de mail.
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('cristian.mello@myserveremail.com', 'cristianc.mello@gmail.com', 
"""
To: cristian.mello@myserveremail.com
From: cristianc.mello@gmail.com

Hello, World!
""")
server.quit()

from urllib.request import urlopen

with urlopen('http://www.google.com') as response:
    for line in response:
        print(line)
        
# IMPORTANTE!
# Para processar requests HTTP, recomenda-se o módulo 'Requests: HTTP for Humans'.
# Link: <http://requests.readthedocs.io/en/master/>