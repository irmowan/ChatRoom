import socket

__author__ = 'irmo'


class ChatServer(socket.socket):
    """ChatServer"""

    def __init__(self, host, port):
        super(ChatServer, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        print("Server Created.")

    def handle_accept(self):
        # The maxinum of clients that could connect to server
        self.maxclients = 5
        # Listen the socket
        self.sock.listen(self.maxclients)
        # Infinite loop to receive messages.
        while True:
            connection, address = self.sock.accept()
            print("Connected by ", address)
            try:
                # connection.settimeout(5)
                buf = connection.recv(1024)
                connection.send(b'Server has received your message.')
                print("Message from client:", buf)
            except socket.timeout:
                print('Time out error.')
            connection.close()

    def close(self):
        self.sock.close()
        print("Server closed.")


if __name__ == '__main__':
    # Set server host and port
    host = 'localhost'
    port = 8002
    # Create a server
    server = ChatServer(host, port)
    server.handle_accept()
    server.close()
