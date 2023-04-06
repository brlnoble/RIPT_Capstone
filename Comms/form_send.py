#!/usr/bin/python3

import socket
import argparse
import sys
import json

from RecvBytes import *

test_json = {
    "bob": 1,
    "george": 2
}

########################################################################
# Echo Server class
########################################################################

class Server:

    HOSTNAME = socket.gethostname()
    PORT = 50000
    
    RECV_BUFFER_SIZE = 1024 # Used for recv.

    MSG_ENCODING = "utf-8" # Unicode text encoding.

    SOCKET_ADDRESS = (HOSTNAME, PORT)

    def __init__(self):
        self.create_listen_socket()
        self.process_connections_forever()

    def create_listen_socket(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind(Server.SOCKET_ADDRESS)
            self.socket.listen()
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
        #print(client)
        
        status, cmd_field = recv_bytes(connection, 32)
        if not status:
            print("Closing connection ...")
            connection.close()
            return
        # Convert the command to our native byte order.
        string_length = int.from_bytes(cmd_field, byteorder='big')
        
        status, json_bytes = recv_bytes(connection, string_length)
        if not status:
            print("Closing connection ...")            
            connection.close()
            return
        if not json_bytes:
            print("Connection is closed!")
            connection.close()
            return

        json_string = json_bytes.decode(Server.MSG_ENCODING)
        form_score = json.loads(json_string)
        print("1")
        print(form_score)
        return form_score
        

########################################################################
# Echo Client class
########################################################################

class Client:

    RECV_SIZE = 1024

    def __init__(self):
        self.send_form(test_json)

    def get_socket(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as msg:
            print(msg)
            exit()

    def connect_to_server(self):
        try:
            self.socket.connect((Server.HOSTNAME, Server.PORT))
        except Exception as msg:
            print(msg)
            exit()

    def send_form(self, form_score):

        print("-" * 72)

        self.get_socket()
        self.connect_to_server()
        print("Connection to ", (Server.HOSTNAME, Server.PORT))
        
        form_string = json.dumps(form_score)
        form_bytes = form_string.encode(Server.MSG_ENCODING)
        string_length = len(form_string).to_bytes(32, byteorder='big')
        pkt = string_length + form_bytes
        
        try:
            self.socket.sendall(pkt)
        except Exception as msg:
            print(msg)
            sys.exit(1)
            
        print("Closing server connection ... ")
        self.socket.close()
            
        # try:
        #     ########################################################
        #     # Read from the connection until the server has closed
        #     # the other end. Then close this end.
        #     ########################################################
        #     while True:
        #         recvd_bytes = self.socket.recv(Client.RECV_SIZE)
        #         if len(recvd_bytes) == 0:
        #             # The server has completed the download and
        #             # has closed the connection. We are done.
        #             print(recvd_bytes_total.decode(Server.MSG_ENCODING))
        #             print("Closing server connection ... ")
        #             self.socket.close()
        #             break
        #         recvd_bytes_total += recvd_bytes
        # except KeyboardInterrupt:
        #     print()
        #     sys.exit(1)


########################################################################
# Process command line arguments if this module is run directly.
########################################################################

# When the python interpreter runs this module directly (rather than
# importing it into another file) it sets the __name__ variable to a
# value of "__main__". If this file is imported from another module,
# then __name__ will be set to that module's name.

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






