import xmlrpc.client
import sys

s = xmlrpc.client.ServerProxy('http://localhost:8000')

input_data = input("Enter data: ")  
s.c_hexa(input_data)

# Print list of available methods
#print(s.system.listMethods())
