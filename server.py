import socket
from threading import Thread
import sys
import time


class Server():
    def __init__(self):
        self.ports = [1000]
        self._msg = ''
        self.start_server()

    def listening1(self):
        l_sock = socket.socket()
        l_sock.bind(('localhost', 9000))
        l_sock.listen(1)
        conn, adr = l_sock.accept()

        while True:
            self._msg = conn.recv(1024)
            if not self._msg:
                break

    def sending(self):
        sock = socket.socket()

        while True:
            try:
                sock.connect(('localhost', self.ports[0]))
                break
            except Exception:
                time.sleep(1)

        while True:
            sock.send(f'{self._msg}\n'.encode())

    def start_server(self):
        lis = Thread(target=self.listening1)
        lis.start()
        send = Thread(target=self.sending)
        send.start()


if __name__ == '__main__':
    server = Server()
    server.start_server()