from srv_main import get_files as get_files_main
from connection import Connection


backup_files = {}


def get_files():
    global backup_files
    backup_files = get_files_main()
    return backup_files


if __name__ == '__main__':
    obj = Connection(9091)
    data = obj.get_data().decode()
    result = get_files()
    obj.send_data(bytes(str(result).encode()))
