import socket

s = socket.socket(AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket()
x = input("What is the IP address you want to connect to?: ")
client_socket.connect((x, 9001))

i = input("What would you like to send to the server?: ")
client_socket.send(i.encode('utf-8'))

data = conn.recv(1024)
print("Received: ", data.decode())
