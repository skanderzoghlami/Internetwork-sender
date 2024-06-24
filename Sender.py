import socket
import os

# The server's hostname or IP address
SERVER_HOST = "192.168.20.1"  # Change to your server's IP address
SERVER_PORT = 5001
# The name of the file we want to send, make sure it exists
FILE = "path/to/your/file.jpg"
# Get the file size
filesize = os.path.getsize(FILE)
SEPARATOR = "<SEPARATOR>"

# Create the client socket
s = socket.socket()

print(f"Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("Connected.")

# Send the filename and filesize
s.send(f"{FILE}{SEPARATOR}{filesize}".encode())

# Start sending the file
with open(FILE, "rb") as f:
    while True:
        # Read the bytes from the file
        bytes_read = f.read(4096)
        if not bytes_read:
            # File transmitting is done
            break
        # We use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)

# Close the socket
s.close()