import socket  # Import socket module to enable network communication
import sys  # Import sys module to interact with the interpreter
from client import handle_connection  # Import the handle_connection function from the client module

port = 9876  # Define the port number on which the server will listen for incoming connections

# Create a new socket using IPv4 addressing and TCP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to all available network interfaces on the specified port
sock.bind(('', port))

# Enable the server to accept connections; the parameter specifies the maximum number of queued connections
sock.listen(1)

while True:
    # Wait for an incoming client connection
    newsock, addr = sock.accept()
    # Call the handle_connection function to manage communication with the connected client
    handle_connection(newsock)
