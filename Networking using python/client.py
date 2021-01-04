import socket
host='127.0.0.1'
port=5000
s=socket.socket()#initialize socket
s.connect((host,port))#connect to the given server
message=input("->")
while message!="quit":
    s.send(message.encode())#send message to the server
    data=s.recv(1024)#receive data from server in 1024 byte at a time
    print("Received from server:" +str(data))
    message=input("->")
s.close
