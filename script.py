import socket
import os
s=socket.socket()
#host=socket.gethostname() #server hostname
host='172.17.8.236'
port=12000 #same as server
s.connect((host,port))
fileToSend = open("ToSend.txt","r")
content = fileToSend.read()
s.send(content.encode())