import socket
import os
    
IP = "192.168.43.155"
SERVER_PORT = 57123
FORMAT ="utf8"

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,SERVER_PORT))
s.listen() 

print("server:",IP,SERVER_PORT)
print("Waiting for Client....") 
while 1:
    conn, addr = s.accept()
    os.system('cls')
    print("!Client connected!")
    print("client address:",addr) 
    print("conn:", conn.getsockname()) 
    a=conn.recv(1024).decode(FORMAT)
    b=conn.recv(1024).decode(FORMAT)
    print("Da nhap 2 so a va b la :", a," va ", b)
    tong = int(a)+ int(b)
    hieu = int(a)- int(b)
    tich = int(a)* int(b)
    thuong = int(a)/ int(b)
    conn.sendall(str(tong).encode(FORMAT))
    conn.recv(1024)
    conn.sendall(str(hieu).encode(FORMAT))
    conn.recv(1024)
    conn.sendall(str(tich).encode(FORMAT))
    conn.recv(1024)
    conn.sendall(str(thuong).encode(FORMAT))
    conn.recv(1024)
    print("Da tra ket qua ve client!!!!")
    conn.close()
