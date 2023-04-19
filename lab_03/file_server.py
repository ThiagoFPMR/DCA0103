import os
from socket import *

server_name = ""
server_port = 61000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)
print("TCP server awaiting connection on the port %d ..." % (server_port))
while True:
    connection_socket, addr = server_socket.accept()
    file_path = connection_socket.recv(1024)
    file_path = file_path.decode("utf-8")
    if os.path.exists(f"files/{file_path}"):
        with open(f"files/{file_path}", "r") as file:
            data = file.read()
    else:
        data = "File not found"
    connection_socket.send(data.encode("utf-8"))
    connection_socket.close()
server_socket.close()
