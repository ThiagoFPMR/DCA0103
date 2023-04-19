from socket import *

server_name = "localhost"
server_port = 60000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

command = input("Enter the command: ")
client_socket.send(command.encode("utf-8"))
output = client_socket.recv(1024)
print(
    "Server (%s, %d) replied:\n%s" % (server_name, server_port, output.decode("utf-8"))
)
client_socket.close()
