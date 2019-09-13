#open("texte.txt", "w") - criação do arquivo
#open("texte.txt", "r") - leitura do arquivo
#meuArquivo.write() - escreve no arquivo

##########################3#######

#################################### Socket #######################
'''
import socket
# Endereco IP do Servidor
HOST = ‘192.168.1.2'
# Porta que o Servidor vai escutar
PORT = 12344
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()
'''

'''
#Servidor TCP
import socket
# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()
'''

'''#Cliente TCP
import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send(msg.encode())
    msg = input()
tcp.close()
'''