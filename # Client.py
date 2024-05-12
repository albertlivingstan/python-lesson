# Client.py
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 12345

# Connect to server
client_socket.connect((host, port))

# Send data to server
client_socket.send('Hello, server!'.encode())

# Receive data from server
response = client_socket.recv(1024)
print('Received:', response.decode())

# Close the connection
client_socket.close()
