import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 9001))
server_socket.listen(5)
conn, address = server_socket.accept()
print("Connection from:", address)
