from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket
import sys


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(('localhost', 8000),requestHandler=RequestHandler)
server.register_introspection_functions()

# Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 20000)
sock.connect(server_address)

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.
server.register_function(pow)

# Register a function under a different name
def adder_function(x, y):
    return x + y
server.register_function(adder_function, 'add')

def convert_to_hexa(x):
    for i in x:
        sock.sendall(hex(ord(i)).encode())
        data = sock.recv(1024)
    
    print('Przeslano dane w postaci heksadecymalnej')
    return x

server.register_function(convert_to_hexa, 'c_hexa')

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'mul').
class MyFuncs:
    def mul(self, x, y):
        return x * y

server.register_instance(MyFuncs())
    
# Run the server's main loop
server.serve_forever()
