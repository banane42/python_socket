import socket
import threading

HOST = "127.0.0.1"
PORT = 42069

class SocketConnection(threading.Thread):
    def __init__(self): 
        threading.Thread.__init__(self)
        self.isDaemon = True
        self.shutdown = False
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    

    def begin(self):
        self.soc.connect((HOST, PORT))
        self.start()

    def stop(self):
        self.shutdown = True

    def run(self):
        while not self.shutdown:
            incoming, address = self.soc.recvfrom(1024)
            print("{}: {}".format(address, str(incoming)))

def main():
    print("Type your message")
    socCon = SocketConnection()
    socCon.begin()

    while True:
        message = input("Me: ")
        if message == "quit":
            socCon.stop()
            break
        else:
            socCon.soc.sendall(message.encode()) 


main()
