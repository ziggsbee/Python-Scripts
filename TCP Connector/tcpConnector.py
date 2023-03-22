#! /bin/python3
import socket

class TCPConnector:

    sock = None
    delim = "\n"

    def __init__(self,hostname, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((hostname, port))

    def setDelimiter(self,value):
        self.delim = value

    def getRequest(self):
        data = self.sock.recv(2048)
        return data.decode()

    def sendRequest(self, value):
        value += self.delim
        self.sock.sendall(value.encode())
        return value
    
    def close(self):
        self.sock.close()
        print("Connection closed.")