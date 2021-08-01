import os
import socket
import tqdm


#object for loading data from client
class Server:

    # creating object data
    def __init__(self):
        self.SERVER_HOST = self.get_ip()                                   # server address
        self.SERVER_PORT = 5001                                       # port address
        self.BUFFER_SIZE = 4096                                       # size of the buffer
        self.SEPARATOR = "<SEPARATOR>"
        print("Init server object")
        self.server_socket = socket.socket()
        self.server_socket.bind((self.SERVER_HOST, self.SERVER_PORT))
        print(f"[*] Listening as {self.SERVER_HOST}:{self.SERVER_PORT}")
        self.server_socket.listen(5)

    # function for getting ip data
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    # function for running server
    def run(self):
        client_socket, address = self.server_socket.accept()
        print("Server is runing...")
        while(True):
            client_socket, address = self.server_socket.accept()
            print(f"[+] {address} is connected.")
            received = client_socket.recv(self.BUFFER_SIZE).decode()
            filename, filesize = received.split(self.SEPARATOR)
            filename = os.path.basename(filename)
            filesize = int(filesize)

            progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "wb") as f:
                while True:
                    bytes_read = client_socket.recv(self.BUFFER_SIZE)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                    progress.update(len(bytes_read))
            f.close()
            print("File saved - ready for another connection")
            # close the client socket
            client_socket.close()
            # close the server socket
            self.server_socket.close()
