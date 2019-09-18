import socket
import ssl
import time

server_sni_hostname = 'example.com' # Muito IMPORTANTE!
server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=server_cert)
# Cria o contexto

context.load_cert_chain(certfile=client_cert, keyfile=client_key)
# Carrega os certificados do cliente

TCP_IP = '127.0.0.1' # Endereco IP do servidor 
TCP_PORTA = 8082       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

MENSAGEM = None

# Criacao de socket TCP do cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

    with context.wrap_socket(cliente,server_hostname=server_sni_hostname) as ccliente:            
        # Conecta ao servidor em IP e porta especifica 
        ccliente.connect((TCP_IP, TCP_PORTA))

        MENSAGEM  = input("Digite sua mensagem para o servidor: ")
        ccliente.send(MENSAGEM.encode('UTF-8')) # envia mensagem para servidor 
        
        ccliente.close()



        