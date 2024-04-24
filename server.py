import socket
import ssl

# Define the SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print("Server is listening on {}:{}".format(*server_address))

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        # Wrap the socket with SSL/TLS
        secure_connection = context.wrap_socket(connection, server_side=True)

        print("Connection from:", client_address)

        # Receive data from the client
        data = secure_connection.recv(1024)
        print("Received:", data.decode())

        # Send a response back to the client
        secure_connection.sendall(b"Hello, client!")

    finally:
        # Close the connection
        secure_connection.close()
