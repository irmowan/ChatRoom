from __future__ import print_function
import socket
import thread
import sys

__author__ = 'irmo'


class ChatServer(socket.socket):
    """docstring for ChatServer"""

    def __init__(self, host, port):
        super(ChatServer, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((host, port))
        except socket.error:
            print('Bind Failed.')
            sys.exit(0)
        self.sock.listen(5)
        print('Socket now listening...')
        self.users = {}

    def handle_accept(self):
        while True:
            conn, addr = self.sock.accept()
            thread.start_new_thread(self.handle_single_connect, (conn, addr))

    def handle_single_connect(self, conn, addr):
        print("New connection from %s:%s", addr)
        username = conn.recv(RECV_BUFFER)
        self.users[username] = conn
        msg = username + " entered the chat room."
        self.broadcast(username, msg + "\n")

        while True:
            raw_request = conn.recv(RECV_BUFFER)
            if not raw_request:
                continue
            print(raw_request)
            self.broadcast(username, username + ": " + raw_request)

        conn.close()

    def broadcast(self, username, content):
        for name, conn in self.users.items():
            if name != username:
                conn.sendall(content)


if __name__ == "__main__":

    RECV_BUFFER = 4096
    HOST = 'localhost'
    PORT = 5000
    server = ChatServer(HOST, PORT)
    try:
        server.handle_accept()
    except KeyboardInterrupt:
        print("Server shutdown.")
    finally:
        server.close()
