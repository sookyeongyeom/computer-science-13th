from http import server
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 2222)
print("Connnecting to %s:%s" % server_address)
sock.connect(server_address)

message = b"To Infinity..."
print(f'Client sending "{message.decode()}"')
sock.sendall(message)

reply = sock.recv(11)
print(f'Client received "{reply.decode()}"')

sock.close()
