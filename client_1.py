import socket

command = (b'0',  # read
           b'1',  # add
           b'2',  # chn
           b'3',  # del
           b'q')  # close

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(command[1])

data = sock.recv(1024).decode()
print(data)
if data is None:
    sock.close()
