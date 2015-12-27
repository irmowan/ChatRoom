# build by python2.7
# telnet program example
import socket
# import select
# import string
import sys
import thread
import Tkinter as tk
from time import sleep

__author__ = 'irmo'


class ChatFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.publicText = tk.Text(self, width=60, height=20)
        self.inputText = tk.Text(self, width=40, height=5)
        self.sendButoon = tk.Button(self, text='send', command=self.__send)
        self.exitButton = tk.Button(self, text='exit', command=self.__exit)
        self.userLabel = tk.Label(self, text='Users:')
        self.userList = tk.Text(self, width=20, height=4)
        self.__create_widgets()
        self.grid()
        thread.start_new_thread(self.__receive_message, ())
        client.sendall(client.username)

    def __create_widgets(self):
        self.publicText.grid(column=0, row=0, columnspan=4)
        self.inputText.grid(column=0, row=1, columnspan=3, rowspan=2)
        self.sendButoon.grid(column=0, row=3)
        self.exitButton.grid(column=2, row=3)
        self.userLabel.grid(column=3, row=1)
        self.userList.grid(column=3, row=2, rowspan=2)

    def __send(self):
        msg = self.inputText.get(1.0, tk.END).strip()
        client.sendall(msg)

    def __receive_message(self):
        while True:
            sleep(SLEEP_TIME)
            try:
                raw_response = client.receive()
                print(raw_response)
            except socket.error:
                continue
            self.publicText.insert(tk.INSERT, raw_response)

    def __exit(self):
        pass

    def add_user(self):
        pass

    def del_user(self):
        pass


class ChatClient(socket.socket):

    def __init__(self, username):
        socket.socket.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.username = username

    def loop(self):
        while True:
            data = raw_input('>>>')
            self.sock.sendall(data)
            print(self.sock.recv(RECV_BUFFER))

    def connect(self, host, port, timeout=10):
        self.sock.connect((host, port))
        self.sock.settimeout(timeout)
        self.connected = True

    def close(self):
        self.sock.close()
        self.connected = False

    def receive(self):
        return self.sock.recv(RECV_BUFFER)

    def sendall(self, message):
        self.sock.sendall(message)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print 'Usage : python client.py hostname port'
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    username = sys.stdin.readline().strip()

    RECV_BUFFER = 4096
    SLEEP_TIME = 0.5

    client = ChatClient(username)
    client.connect(host, port)
    app = ChatFrame()
    app.master.title('chat room')
    app.mainloop()
