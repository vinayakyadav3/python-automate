import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

# Accept a client connection
client_socket, client_address = server_socket.accept()

# Send and receive data
client_socket.sendall(b'Hello, client!')
data = client_socket.recv(1024)

# Close the socket
client_socket.close()
server_socket.close()
