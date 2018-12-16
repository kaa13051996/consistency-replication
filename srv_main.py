from hashlib import sha1
import socket

list_files = ['file_1', 'file_2', 'file_3']


def get_files():
    hash_files = [sha1(str.encode(item)).hexdigest() for item in list_files]
    files = dict(zip(hash_files, list_files))
    return files


def del_files(index=3):
    if check_index(int(index)):
        del list_files[index]
        return get_files()
    else:
        print('Указан ошибочный индекс!')


def add_files(name_files='file_4'):
    list_files.append(name_files)
    return get_files()


def chn_name_files(index=3, name='file_4v2'):
    if check_index(int(index)):
        list_files.insert(index, str(name))
        del_files(index + 1)
        return get_files()
    else:
        print('Указан ошибочный индекс!')


def check_index(index):
    return True if 0 <= index < len(list_files) else False


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('localhost', 9090))
    sock.listen(4)
    while True:
        try:
            conn, addr = sock.accept()
            data = conn.recv(1024).decode()
            if data == '1':
                result = add_files()
            elif data == '2':
                result = chn_name_files()
            elif data == '3':
                result = del_files()
            else:
                result = get_files()
            conn.send(bytes(str(result).encode()))
        except Exception as ex:
            print('Error: {}!'.format(ex.args[1]))
