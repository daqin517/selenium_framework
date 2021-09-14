import socket,os

server_address = ('10.157.49.167',5006)
client_address = ('10.157.49.166',5006)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(server_address)

s.listen(1)

while 1:
    conn,addr = s.accept()
    print('Connected by',addr)
    while 1:
        data = conn.recv(1024)
        cmd_status,cmd_result = os.system(data)
        if len((cmd_result.strip())) == 0:
            conn.sendall('Done.')
            break
        else:
            conn.sendall(cmd_result)
    conn.close()