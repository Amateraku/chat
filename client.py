import socket
import sys
import time
from threading import Thread


def incoming_handler(host, port):
    in_sock = socket.socket()
    in_sock.bind((host, port))
    in_sock.listen(1)
    conn, addr = in_sock.accept()
    print(f'Start listening on: {host}:{port}')

    while True:
        _msg = conn.recv(1024)
        if not _msg:
            break
        else:
            print(f"> {_msg.decode().strip()}")


if __name__ == '__main__':
    in_host = out_host = 'localhost'
    in_port, out_port = int(sys.argv[1]), int(sys.argv[2])

    incoming_thread = Thread(target=incoming_handler, args=(in_host, in_port, ))
    incoming_thread.start()

    sock = socket.socket()
    while True:
        try:
            sock.connect((out_host, out_port))
            break
        except Exception:
            time.sleep(1)

    print(f"Connected to {out_host}:{out_port}")
    while True:
        msg = input()
        sock.send(f'{msg}\n'.encode())
