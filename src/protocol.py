tfrom time import time
from datetime import datetime
__author__ = 'irmo'


class Protocol(object):
    """docstring for Protocol
    A protocol includes three arguments(protocol version, uri, and protocol type),
    a header, and a data entity contains data.
    """

    def __init__(self):
        super(Protocol, self).__init__()
        self.header = Header()
        self.dataEntity = DataEntity()

    def set_version(self, version='Protocol'):
        self.version = version

    def set_uri(self, uri):
        self.uri = uri

    def set_type(self, reqtype):
        self.type = reqtype


class Header(object):
    """docstring for Header
    Header is the header of the protocol,
    it includes many key-value pairs, including time,
    name, date length and so on, if needed.
    """

    def __init__(self):
        super(Header, self).__init__()
        self.dict = {}

    def set_time(self, time):
        self.dict['time'] = str(float(time))

    def set_name(self, name):
        self.dict['name'] = name

    def set_datalen(self, dataEntity):
        self.dict['datalen'] = str(len(dataEntity.data))

    def pack(self):
        package = ''
        for key, value in self.dict.iteritems():
            package += (str(key) + ': ' + str(value) + '\n')
        return package

    def unpack(self, lines):
        for line in lines:
            key_value = line.split(': ', 1)
            key = key_value[0]
            value = key_value[1]
            self.dict[key] = value


class DataEntity(object):
    """docstring for DataEntity
    Data entity contains the data.
    """

    def __init__(self):
        super(DataEntity, self).__init__()
        self.data = ''

    def set_data(self, data):
        self.data = data

    def pack(self):
        return self.data

    def unpack(self, package):
        self.data = package


class Request(Protocol):
    """docstring for Request
    Request inherits from Protocol
    'generate' generate a Request from arguments
    'pack' packs the Request to a package
    'unpack' unpacks the package to a protocol
    """

    def __init__(self):
        super(Request, self).__init__()

    def generate(self, uri, port, reqtype, time, name, data):
        self.set_version()
        self.set_uri(uri + ":" + str(port))
        self.set_type(reqtype)
        self.header.set_time(time)
        self.header.set_name(name)
        self.dataEntity.set_data(data)
        self.header.set_datalen(self.dataEntity)

    def pack(self):
        package = ''
        package += self.version + ' '
        package += self.uri + ' '
        package += self.type + ' '
        package += '\n'
        package += self.header.pack()
        package += self.dataEntity.pack()
        return package

    def unpack(self, package):
        lines = package.split('\n')
        request_line = lines[0].split(' ')
        self.protocol = request_line[0]
        self.uri = request_line[1]
        self.type = request_line[2]
        self.header.unpack(lines[1:4])
        self.dataEntity.unpack(''.join(lines[4:]))

    def get_uri(self):
        return self.uri

    def get_type(self):
        return self.type

    def get_time(self):
        if 'time' in self.header.dict.keys():
            return float(self.header.dict['time'])

    def get_name(self):
        if 'name' in self.header.dict.keys():
            return self.header.dict['name']

    def get_datalen(self):
        if 'datalen' in self.header.dict.keys():
            return int(self.header.dict['datalen'])

    def get_data(self):
        return self.dataEntity.data


def read_time(timestamp):
    """ Change the timestamp in package to datetime"""
    return str(datetime.fromtimestamp(int(timestamp)))


def generateRequest(host, port, reqtype, username, data=''):
    """ Generate a request package"""
    req = Request()
    req.generate(host, port, reqtype, time(), username, data)
    package = req.pack()
    return package


def handleReuest(package):
    """ Unpack the package received"""
    req = Request()
    req.unpack(package)
    return req
