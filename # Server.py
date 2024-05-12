# Server.py
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Now wait for client connection
server_socket.listen(5)

while True:
    # Establish connection with client
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)
    data = client_socket.recv(1024)
    print('Received:', data.decode())
    client_socket.send('Message received'.encode())
    client_socket.close()
