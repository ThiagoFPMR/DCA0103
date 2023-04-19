from socket import *

server_name = "localhost"
server_port = 60000
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input("Enter the message to the server: ")
client_socket.sendto(message.encode("utf-8"), (server_name, server_port))
response, server_address = client_socket.recvfrom(2048)
print(
    "Server (%s, %d) replied:\n%s"
    % (server_name, server_port, response.decode("utf-8"))
)
client_socket.close()
