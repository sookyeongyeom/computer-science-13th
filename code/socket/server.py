from http import server
import socket

# TCP/IP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 연결
server_address = ("localhost", 2222)
sock.bind(server_address)

# 클라이언트로부터의 연결을 감청
sock.listen(1)
print("Waiting for a client to connect")
client, client_port = sock.accept()
print("Connection from client %s:%s" % client_port)

# 클라이언트로부터의 요청을 수신
request = client.recv(14)
print(f'Client sent "{request.decode()}"')

# 응답 송신
reply = b"And Beyond!"
print(f'Server replies "{reply.decode()}"')
client.sendall(reply)

client.close()
