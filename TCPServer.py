from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
# 외부 while True: 새 클라이언트 연결 대기
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected from {addr[0]}:{addr[1]}')
    # 내부 while True: 같은 클라이언트로부터 메시지 계속 수신
    # recv()가 빈 문자열 반환 시(Ctrl+C 등으로 클라이언트 종료) 루프 탈출 후 소켓 닫음
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if not sentence:  # 클라이언트가 연결을 종료하면 빈 문자열 반환
            break
        capitalizedSentence = sentence.upper()
        print(f'Received from {addr[0]}:{addr[1]} -> {capitalizedSentence}')
        connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
    print(f'Connection closed from {addr[0]}:{addr[1]}')
