import socket
import ssl

# Define the SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("server.crt")

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 10000)
client_socket.connect(server_address)

try:
    # Wrap the socket with SSL/TLS
    secure_connection = context.wrap_socket(client_socket, server_hostname="localhost")

    # Send data to the server
    secure_connection.sendall(b"Hello, server!")

    # Receive a response from the server
    data = secure_connection.recv(1024)
    print("Received:", data.decode())

finally:
    # Close the connection
    secure_connection.close()
