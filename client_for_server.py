import socket
import sys
import time
from threading import Thread


def listening(host, port):
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(1)
    conn, adr = sock.accept()

    while True:
        msg = conn.recv(1024)
        if not msg:
            break


if __name__ == '__main__':
    host = 'localhost'

    lis = Thread(target=listening, args=(host, 1000))
    lis.start()

    sock = socket.socket()
    while True:
        try:
            sock.connect((host, 5000))
            break
        except Exception:
            time.sleep(1)

    while True:
        msg = input()
        sock.send(f'{msg}\n'.encode())