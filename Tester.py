# Jakub Wawak
# all rights reserved 2021
# kubawawak@gmail.com
import socket
import os
import tqdm
class Tester:

    # constructor for preparing internal data of object
    def __init__(self,host):
        self.host = host
        self.port = 5001
        self.socket = socket.socket()
        self.connected = False
        self.SEPARATOR = "<SEPARATOR>"
        self.BUFFER_SIZE = 4096  # send 4096 bytes each time step

    # function for connecting to server
    def connect(self):
        try:
            print(f"[+] Connecting to {self.host}:{self.port}")
            self.socket.connect((self.host, self.port))
            print("[+] Connected.")
            self.connected = True
        except:
            print("Error connecting to host")

    # function for sending things to server
    def send(self,file_path):
        if os.path.exists(file_path):
            print("File found")
            print("Preparing file to send")
            filesize = os.path.getsize(file_path)
            self.socket.send(f"{file_path}{self.SEPARATOR}{filesize}".encode())
            progress = tqdm.tqdm(range(filesize), f"Sending {file_path}", unit="B", unit_scale=True, unit_divisor=1024)
            with open(file_path, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(self.BUFFER_SIZE)
                    if not bytes_read:
                        # file transmitting is done
                        break
                    # we use sendall to assure transimission in
                    # busy networks
                    self.socket.sendall(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))
            # close the socket
            self.socket.close()

        else:
            print("File not found - cannon send")
