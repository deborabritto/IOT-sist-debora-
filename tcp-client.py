import socket

HOST = 'localhost'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

tcp.connect(destino)

while(True):
    msg = bytes(input('Digite a mensagem: '), encoding='utf8')
    tcp.send(msg)

tcp.close()