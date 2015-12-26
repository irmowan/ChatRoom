import socket
import time

__author__ = 'irmo'


class ChatClient(socket.socket):
    """ChatClient"""

    def __init__(self, host, port):
        super(ChatClient, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Client created.")

    def do_send(self, host, port):
        self.sock.connect((host, port))
        # s = raw_input()
        self.sock.send(b'hello world!')
        print(self.sock.recv(1024))


if __name__ == '__main__':
    # Set host and port connect to.
    host = 'localhost'
    port = 8002
    # Create a new Client
    client = ChatClient(host, port)
    client.do_send(host, port)
    client.close()
