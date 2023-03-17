
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect(("www.example.com", 80))

s.sendall(b"Hello, world!")

data = s.recv(1024)

s.close()

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8888               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Server listening on port', PORT)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    conn.sendall(b'Hello, client!')
    conn.close()

    
    
import socket

HOST = 'localhost'        # The remote host
PORT = 8888               # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, server!')
    data = s.recv(1024)

print('Received', repr(data))



import requests

response = requests.get("https://www.example.com")
print(response.text)

import requests

data = {"username": "alice", "password": "secret"}
response = requests.post("https://www.example.com/login", data=data)
print(response.text)


import requests

response = requests.get("https://api.github.com/repos/requests/requests")
data = response.json()
print(data["description"])


import requests

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get("https://www.example.com", headers=headers)
print(response.text)

