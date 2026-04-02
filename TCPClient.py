from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
# TCP는 연결 지향형이므로 connect()로 서버와 3-way handshake 수행
# 클라이언트 포트 번호는 OS가 임시 포트(ephemeral port)를 랜덤 할당함. 실행마다 달라짐.
clientSocket.connect((serverName, serverPort))

try:
    while True:
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence.decode())
finally:
    clientSocket.close()
