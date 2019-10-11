import socket

Port = 50007
Destination = "192.168.0.9"
#ここには自分のPCのIPアドレスを入れてください(NetEnumを使えばわかります)



class SocketCommunication_C():

    def __init__(self,s):
        self.port = Port
        self.dest = Destination
        self.s = s
        
    def setup(self):
        self.s.connect((self.dest, self.port))
        print("Connected")

    def senddata(self,string):
        self.s.sendall(string.encode())
    
    def receivedata(self):
        return self.s.recv(1024).decode()

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        sc = SocketCommunication_C(s)
        sc.setup()
        sc.senddata("Hello World!")