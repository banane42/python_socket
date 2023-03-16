import socket

HOST = "127.0.0.1"
PORT = 42069

def main():
    print("Hello Server World")
    lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lSocket.bind((HOST, PORT))
    lSocket.listen()
    conn, addr = lSocket.accept()

    messageCount = 0

    while True:
        data = conn.recv(1024)
        print(f"{addr} sent {data}")
        if not data:
            print("Recieved disconnect from client")
            conn.sendall(str(messageCount).encode())
            break
        else:
            print("upping message count")
            messageCount += 1
        conn.sendall("ack".encode())

main()
