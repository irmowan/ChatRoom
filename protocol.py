import time

__author__ = 'irmo'


class Protocol(object):
    """docstring for Protocol"""
    "host, port, time, tyte, name, length, data"
    def __init__(self, name):
        super(Protocol, self).__init__()
        self.http_version = 'HTTP/1.1'
        self.name = username
        self.data = None

class Request(Protocol):
    """docstring for Request"""

    def __init__(self, arg):
        super(Request, self).__init__()
        self.arg = arg


class Response(Protocol):
    """docstring for Response"""

    def __init__(self, arg):
        super(Response, self).__init__()
        self.arg = arg
