import socket
Port = 50007


class SocketCommunication_S():
    def __init__(self,s):
        self.port = Port
        self.s = s

    def setup(self):
        self.s.bind(('', self.port))
        self.s.listen(1)
        print("Waiting now...")
        conn, addr = s.accept()
        self.conn = conn
        print("Connecting to {}.".format(addr))

    def senddata(self,string):
        self.conn.sendall(string.encode())
    
    def receivedata(self):
        return self.conn.recv(1024).decode()


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        sc = SocketCommunication_S(s)
        sc.setup()
        a = sc.receivedata()
        print(a)