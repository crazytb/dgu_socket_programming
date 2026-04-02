from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 클라이언트 포트 번호는 bind()를 호출하지 않으므로,
# sendto() 시점에 OS가 임시 포트(ephemeral port)를 랜덤 할당함. 실행마다 달라짐.

try:
    while True:
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modified_message, server_address = clientSocket.recvfrom(2048)
        print(modified_message.decode())
finally:
    clientSocket.close()