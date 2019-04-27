#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Limpando a tela
subprocess.call('clear', shell=True)

# Esperando o ip
remoteServer    = raw_input("Digite o host remoto: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Imprime um banner com informacoes sobre qual host vamos escanear
print "-" * 60
print "Aguarde, escaneando o host remoto", remoteServerIP
print "-" * 60

# Checa que horas o scan foi iniciado
t1 = datetime.now()

# Usando uma funcao range para especificar portas (ele vai varrer todas as portas entre 1 e 1024)

# Vai identificar e tratar erros

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Voce pressionou CTRL+c"
    sys.exit()

except socket.gaierror:
    print 'O hostname nao pode ser encontrado. Saindo'
    sys.exit()

except socket.error:
    print "Nao foi possivel conectar ao servidor"
    sys.exit()

# Verificando a hora novamente
t2 = datetime.now()

# Calcula a diferenca de tempo, para ver quanto tempo demorou para executar o script
total =  t2 - t1

# Imprimindo as informacoes na tela
print 'Escaneamento completo em: ', total
