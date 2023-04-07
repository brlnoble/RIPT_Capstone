#!/usr/bin/env python3

########################################################################

import socket
import argparse
import sys
import json
import pprint

########################################################################
# Echo-Server class
########################################################################

class Server:

    HOST = "localhost"
    # HOST = "127.0.0.1"
    # HOST = ""
    # HOST = "0.0.0.0"
    PORT = 50000

    MSG = "Greetings! Thank-you for connecting!"

    RECV_SIZE = 2048
    BACKLOG = 10
    MSG_ENCODING = "utf-8"

    def __init__(self):
        self.create_listen_socket()
        self.process_connections_forever()

    def create_listen_socket(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind( (Server.HOST, Server.PORT) )
            self.socket.listen(Server.BACKLOG)
            print("Listening on port {} ...".format(Server.PORT))
        except Exception as msg:
            print(msg)
            sys.exit(1)

    def process_connections_forever(self):
        try:
            while True:
                self.connection_handler(self.socket.accept())
        except Exception as msg:
            print(msg)
        except KeyboardInterrupt:
            print()
        finally:
            self.socket.close()
            sys.exit(1)

    def connection_handler(self, client):
        connection, address_port = client
        print("-" * 72)
        print("Connection received from {}.".format(address_port))

        rx_data_bytes = connection.recv(Server.RECV_SIZE)
        rx_data_decoded = rx_data_bytes.decode('utf-8')

        # Read the received message as JSON.
        rx_object = json.loads(rx_data_decoded)

        print(type(rx_object))
        print(rx_object)

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(rx_object)

########################################################################
# Echo-Client class
########################################################################

class Client:

    SERVER = "localhost"
    RECV_SIZE = 256

    # Read the input file that is already in JSON format.
    json_file = open("json_employee_database_json.txt", 'r')
    json_data = json_file.read()

    json_data_bytes = json_data.encode('utf-8')

    def __init__(self):
        self.get_socket()
        self.connect_to_server()
        self.connection_send()

    def get_socket(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as msg:
            print(msg)
            sys.exit(1)

    def connect_to_server(self):
        try:
            self.socket.connect((Client.SERVER, Server.PORT))
        except Exception as msg:
            print(msg)
            sys.exit(1)

    def connection_send(self):
        try:
            self.socket.sendall(Client.json_data_bytes)
        except Exception as msg:
            print(msg)
            sys.exit(1)

########################################################################
# Process command line arguments if run directly.
########################################################################

if __name__ == '__main__':
    roles = {'client': Client,'server': Server}
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--role',
                        choices=roles, 
                        help='server or client role',
                        required=True, type=str)

    args = parser.parse_args()
    roles[args.role]()

########################################################################






