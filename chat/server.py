import socket

HOST = "127.0.0.1"
PORT = 42069

def main():
    lSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    lSocket.bind((HOST, PORT))

    clients = []

    while True:
        data, address = lSocket.recvfrom(1024)
        print("Data: {}".format(data))

        if address not in clients:
            clients.append(address)

        for c in clients:
            print(address)
            print(c)
            if address != c:
                lSocket.sendto(data, c)
main()
