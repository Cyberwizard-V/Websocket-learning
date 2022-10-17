#Simple socket -> server setup
import socket

def server_side():
    #HOST and PORT
    HOST = "127.0.0.1" # -> Localhost
    PORT = 65432 # -> Port to listen

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, address = s.accept()
        while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

if __name__ == '__main__':
    server_side()

        