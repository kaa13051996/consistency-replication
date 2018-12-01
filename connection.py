import socket


class Connection:

    def __init__(self, port):
        self.sock = socket.socket()
        self.sock.bind(('localhost', port))
        self.sock.settimeout(20)
        self.sock.listen(4)
        self.conn, self.addr = self.sock.accept()
        print('connected:', self.addr)

    def get_data(self):
        data = self.conn.recv(1024)
        return data

    def send_data(self, data):
        self.conn.send(data)
        if data is None:
            self.conn.close()


if __name__ == '__main__':
    obj = Connection()
    obj.get_data()
