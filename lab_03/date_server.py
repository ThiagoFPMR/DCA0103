import time
from socket import *

server_name = ""
server_port = 60000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((server_name, server_port))
print("TCP server awaiting connection on the port %d ..." % (server_port))
while True:
    message, addr = server_socket.recvfrom(2048)
    message = message.decode("utf-8")
    print("Client %s sent: %s" % (addr, message))
    if message == "date":
        output = str(time.ctime())
    else:
        output = "Unknown command"
    server_socket.sendto(output.encode("utf-8"), addr)
server_socket.close()
