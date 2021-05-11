 
import socket
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 20000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('Received: ',data.decode('UTF-8'))
            if not data:
                break
            conn.sendall(data)
