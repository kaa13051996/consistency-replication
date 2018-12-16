import socket

command = (b'0',  # read
           b'1',  # add
           b'2',  # chn
           b'3')  # del

sock = socket.socket()
sock.connect(('localhost', 9000))  # port 9090: main; 9000: srv;
sock.send(command[3])

data = sock.recv(1024).decode()
sock.close() if data is None else print(data)
