#! /bin/python3
import socket

class TCPConnector:

    sock = None

    def __init__(self,hostname, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((hostname, port))

    def getRequest(self):
        data = self.sock.recv(2048)
        return data.decode()

    def sendRequest(self, value):
        value += "\n"
        self.sock.sendall(value.encode())
        return value
    
    def close(self):
        self.sock.close()
        print("Connection closed.")