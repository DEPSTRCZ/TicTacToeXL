import socket

class Client:

    def __init__(self):

        self.__username = input("Enter Username: ")
        self.__client_socket = socket.socket()

        connecting = True

        while connecting:
            self.__host = input("Enter Host: ")
            self.__host = self.__host if self.__host != 'localhost' else socket.gethostname()
            self.__port = input("Enter Port: ")
            self.__port = 5000
            try:
                self.__client_socket.connect((self.__host, self.__port))
                connecting = False
            except socket.error as e:
                print("\x1b[0;31;40m" + "Failed to connect to server: " + str(e) + "\x1b[0m")


    def go(self):

        while True:
            self.__message = input("Enter Message: ") 
            self.__client_socket.send(self.__message.encode())
            self.__data = self.__client_socket.recv(1024).decode()
            print("Server: " + self.__data)

        self.__client_socket.close()

if __name__ == '__main__':
    client = Client()
    client.go()