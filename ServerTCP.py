import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl

server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED 
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

TCP_IP = '127.0.0.1' # endereço IP do servidor 
TCP_PORTA = 8082       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer

with socket.socket(AF_INET,SOCK_STREAM) as servidor:
    servidor.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # Socket fechado pode ser reutilizado

    # IP e porta que o servidor deve aguardar a conexão
    servidor.bind((TCP_IP, TCP_PORTA))

    #Define o limite de conexões. 
    servidor.listen(5)

    with context.wrap_socket(servidor, server_side=True) as sservidor:
        while True:
            print("Servidor dispoivel na porta %s e escutando....." %TCP_PORTA) 
            
            # Aceita conexão 
            conn, addr = sservidor.accept()
            print ('Endereço conectado:', addr)
            
            #dados retidados da mensagem recebida
            data = conn.recv(TAMANHO_BUFFER)
            if data: 
                print ("Mensagem recebida:", data)  
            
            if data == b'quit':
                print('Fechando Servidor....')
                conn.close()
                exit(0)

