import socket

# Server's IP address
# If the server is not on this machine, 
# put the private (network) IP address (e.g., 192.168.1.5)
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# Receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# Create the server socket
# TCP socket
s = socket.socket()
# Bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
# Listening for incoming connections
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT}...")

# Accept any connection
client_socket, address = s.accept() 
print(f"{address} is connected.")

# Receive the file infos
# Receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# Remove absolute path if there is
filename = filename.split("/")[-1]
# Convert to integer
filesize = int(filesize)

# Start receiving the file from the socket
# and writing to the file stream
with open(filename, "wb") as f:
    while True:
        # Read 4096 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # Nothing is received
            # File transmitting is done
            break
        # Write to the file the bytes we just received
        f.write(bytes_read)

# Close the client socket
client_socket.close()
# Close the server socket
s.close()