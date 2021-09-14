import socket,os

server_address = ('10.157.49.167',5006)
client_address = ('10.157.49.166',5006)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(server_address)
while True:
    cmd = input('Please input cmd:')
    # cmd = r'ls'
    # print(type(cmd.encode()))
    # print(cmd.encode())
    s.send(cmd.encode())
    # s.sendall(cmd)
    data = s.recv(1024)
    print(data)
s.close()