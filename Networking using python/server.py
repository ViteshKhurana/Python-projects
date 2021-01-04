import socket
host='127.0.0.1' #local address of our system
port=5000 #port no
s=socket.socket() #created or initialize socket
s.bind((host,port))#binds host and port for creating server

s.listen(1) #listen only one client at a time
c, addr=s.accept() #this returns client and address of client
print("Connection from:" + str(addr))

while True:
    data= c.recv(1024) #here we receice data from client in 1024 bytes packets
    if not data:
        break
    print("form connected client:" +str(data))
    data= str(data).upper()
    c.send(data.encode()) #sending data to user and encoding it in byte format
c.close()
