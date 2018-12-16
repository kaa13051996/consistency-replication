import socket


def get_files():
    sock_main = socket.socket()
    sock_main.connect(('localhost', 9090))
    sock_main.send(b'0')
    backup_files = sock_main.recv(1024).decode()
    return backup_files


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('localhost', 9000))
    sock.listen(4)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024).decode()
        result = get_files()
        conn.send(bytes(str(result).encode()))
