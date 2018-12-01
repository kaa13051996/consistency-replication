from hashlib import sha1
import connection

list_files = ['file_1', 'file_2', 'file_3']


def get_files():
    hash_files = [sha1(str.encode(item)).hexdigest() for item in list_files]
    files = dict(zip(hash_files, list_files))
    return files


def del_files(index=3):
    if check_index(int(index)):
        del list_files[index]
        return event()
    else:
        print('Указан ошибочный индекс!')


def add_files(name_files='file_4'):
    list_files.append(name_files)
    return event()


def chn_name_files(index=3, name='file_4v2'):
    if check_index(int(index)):
        list_files.insert(index, str(name))
        del_files(index + 1)
        return event()
    else:
        print('Указан ошибочный индекс!')


def event():
    print('Были произведены изменения')
    return get_files()


def check_index(index):
    if 0 <= index < len(list_files):
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        try:
            obj = connection.Connection(9090)
            data = obj.get_data().decode()
            command = {'0': get_files(),
                       '1': add_files(),
                       '2': chn_name_files(),
                       '3': del_files()}
            result = command.get(data)
            obj.send_data(bytes(str(result).encode()))
        except Exception as ex:
            print('Error: {}!'.format(ex.args[1]))
        # finally:
        #     obj.send_data(bytes(str(None).encode()))
