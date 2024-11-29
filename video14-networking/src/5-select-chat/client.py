import socket  # Import socket module for network communication
import sys  # Import sys module to interact with the interpreter
import select  # Import select module to monitor I/O streams
from time import sleep  # Import sleep function from time module to pause execution

port = 9876  # Define the port number to connect to
ip = '127.0.0.1'  # Define the IP address of the server

def handle_connection(sock):
    """
    Handles the communication between the client and the server.
    
    Args:
        sock (socket.socket): The socket object representing the connection.
    """
    while True:
        # Monitor the socket and standard input for any incoming data
        rd, _, _ = select.select([sock, sys.stdin], [], [])
        
        if sys.stdin in rd:
            try:
                # Read a line of input from the user
                keytext = sys.stdin.readline()
            except EOFError:
                # Exit the program if an EOF is encountered
                sys.exit()

            # Encode the user input to bytes
            encoded_text = keytext.encode()
            try:
                # Send the encoded text to the server
                sock.send(encoded_text)
            except BrokenPipeError:
                # Handle the case where the server has disconnected
                print("remote site disconnected")
                return

        if sock in rd:
            # Receive data from the server
            encoded_text = sock.recv(1024)
            if len(encoded_text) == 0:
                # If no data is received, the server has closed the connection
                sock.close()
                break
            # Decode the received bytes to a string
            text = encoded_text.decode()
            # Display the received message to the user
            print(">>", text, "<<")

if __name__ == "__main__":
    # Create a new TCP socket using IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            # Attempt to connect to the server using the specified IP and port
            sock.connect((ip, port))
            break  # Exit the loop if connection is successful
        except ConnectionRefusedError:
            # Inform the user that the server is not yet available
            print("waiting for server...")
            sock.close()  # Close the current socket
            # Create a new socket for the next connection attempt
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sleep(1)  # Wait for 1 second before retrying

    # Start handling the connection once connected
    handle_connection(sock)