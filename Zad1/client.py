import xmlrpc.client
import sys

s = xmlrpc.client.ServerProxy('http://localhost:8000')

a = int(sys.argv[1])
b = int(sys.argv[2])
print('Zadanie1 - dodawanie: ' + str(s.add(a,b)))
#print(s.pow(2,3))  # Returns 2**3 = 8
#print(s.add(2,3))  # Returns 5
#print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
#print(s.system.listMethods())
