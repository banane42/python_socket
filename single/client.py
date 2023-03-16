import socket
import time

HOST = "127.0.0.1"
PORT = 42069

def main():
    print("Hello Client World")
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))
    
    #soc.sendall(b"Hello, world")
    #data = soc.recv(1024)
    #print(f"Recieved {data!r}")
    count = 0
    while count < 10:
        payload = ("count: " + str(count))
        print(f"Sending Payload: {payload}")
        soc.sendall(payload.encode())
        count += 1
        time.sleep(0.25)
    
    #soc.sendall(b'') 
    data = soc.recv(1024)   
    print(f"Recieved {data!r}")
    time.sleep(5)
    #soc.sendall("rcv".encode())
    #data = soc.recv(1024)
    #print(f"Recivied {data!r}")
    
main()
