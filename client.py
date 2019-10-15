import yaml 
import json
import socket
from datetime import datetime
from argparse import ArgumentParser


def make_request(action, text, date=datetime.now()): #добавим в запрос action, чтобы уточнить цель запроса + время запроса
    return {
        'action': action,
        'data': text,
        'time': date.timestamp()
    }


if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'port': 8000,
        'buffersize': 1024,
    }

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=False,
                        help='Sets config path')
    parser.add_argument('-ht', '--host', type=str, required=False,
                        help='Sets server host')
    parser.add_argument('-p', '--port', type=str, required=False,
                        help='Sets server port')

    args = parser.parse_args()

    if args.config: # если в ком строку был передан адрес файла конфиг, то
        with open(args.config) as file:
            file_config = yaml.safe_load(file)
            config.update(file_config or {}) #если в файле ничего нет, то config.udate({}) оставит всё как и было

    host = args.host if args.host else config.get('host')
    port = args.port if args.port else config.get('port')
    buffersize = config.get('buffersize')

    sock = socket.socket()
    sock.connect((host, port))

    action = input('Enter action name: ')
    message = input('Enter your message: ')

    request = make_request(action, message)
    string_request = json.dumps(request)

    sock.send(string_request.encode())
    bytes_response = sock.recv(buffersize)

    response = json.loads(bytes_response)
    print(response)

    sock.close()