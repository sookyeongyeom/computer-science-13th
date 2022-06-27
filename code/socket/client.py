from http import server
import socket

# TCP/IP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 연결
server_address = ("localhost", 2222)
print("Connnecting to %s:%s" % server_address)
sock.connect(server_address)

# 요청 메시지 전송
message = b"To Infinity..."
print(f'Client sending "{message.decode()}"')
sock.sendall(message)

# 서버로부터의 응답을 수신
reply = sock.recv(11)
print(f'Client received "{reply.decode()}"')

sock.close()
