import socket

class Server:
    def __init__(self):

        self.__host = socket.gethostname()
        self.__port = int(input("Enter Port: "))
        self.__port = 5000 if self.__port == '' else self.__port

        self.__server_socket = socket.socket()  # get instance
        self.__server_socket.bind((self.__host, self.__port))

    def listen(self):
        print("Listening on port " + str(self.__port) + "...")
        self.__server_socket.listen(2)
        self.__conn, self.__address = self.__server_socket.accept()

        print("Connection from: " + str(self.__address))

        while True:

            self.__recieved_data = self.__conn.recv(1024).decode()
            if not self.__recieved_data:
                break
            print(str(self.__address) + ": " + str(self.__recieved_data))
            self.__conn.send(self.__recieved_data.encode())

        self.__conn.close()

if __name__ == '__main__':
    server = Server()
    server.listen()