from protocol import *

HOST = 'localhost'
PORT = 5000
req = Request()
req.generate(HOST, PORT, 'SEND', time.time(), 'irmo', 'hello, world!')
p = req.pack()
print(p)
print
newreq = Request()
newreq.unpack(p)
print(newreq.uri)
print(newreq.type)
print(newreq.header.dict['name'])
print(newreq.header.dict['time'])
print(newreq.header.dict['datalen'])
print 'data:', newreq.dataEntity.data 
