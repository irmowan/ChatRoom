# build by python2.7
# telnet program example
import socket
import select
import string
import sys
import Tkinter as tk


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


class ChatFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.publicText = tk.Text(self, width=60, height=20)
        self.inputText = tk.Text(self, width=40, height=5)
        self.sendButoon = tk.Button(self, text='send', command=self.send)
        self.exitButton = tk.Button(self, text='exit', command=self.exit)
        self.userLabel = tk.Label(self, text='Users:')
        self.userList = tk.Text(self, width=20, height=4)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.publicText.grid(column=0, row=0, columnspan=4)
        self.inputText.grid(column=0, row=1, columnspan=3, rowspan=2)
        self.sendButoon.grid(column=0, row=3)
        self.exitButton.grid(column=2, row=3)
        self.userLabel.grid(column=3, row=1)
        self.userList.grid(column=3, row=2, rowspan=2)

    def send(self):
        pass

    def exit(self):
        pass

    def add_user(self):
        pass

    def del_user(self):
        pass

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print 'Usage : python telnet.py hostname port'
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    username = sys.stdin.readline()
    app = ChatFrame()
    app.master.title('Chatroom')
    app.mainloop()


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()

    print 'Connected to remote host. Start sending messages'
    prompt()

    while True:
        rlist = [sys.stdin, s]

        # Get the list sockets which are readable
        read_list, write_list, error_list = select.select(rlist, [], [])

        for sock in read_list:
            # incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # print data
                    sys.stdout.write(data)
                    prompt()

            # user entered a message
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
