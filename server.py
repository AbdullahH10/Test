import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("")
print("Server is running on host:",host)
print("")
port=8080
s.bind((host,port))
print("")
print('Server successfully binded to host and port')
print("")
print("waiting for incomig connection")
print("")
s.listen(1)
conn,addr=s.accept()
print(addr,"connected to server and is online...")
print("")
while 1:
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    print("message has been sent")
    print("")
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("Client:",incoming_message)
    print("")
