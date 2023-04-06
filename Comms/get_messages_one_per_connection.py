#!/usr/bin/env python3

########################################################################
# GET Messages
#
# In this version, the server immediately closes the TCP connection
# when the message has been sent. This is used as a signal to the
# client that the message download is complete. To do multiple GETs,
# the client creates new TCP connections.
#
########################################################################

import socket
import argparse
import time
import sys
import StringSamples
import random
import binascii

from RecvBytes import *

GET_REQUEST = b'GET'
GET_REQUEST_SIZE = len(GET_REQUEST)

########################################################################
# SERVER
########################################################################

class Server:

    HOSTNAME = socket.gethostname()
    PORT = 50000

    RECV_SIZE = 100

    BACKLOG = 5

    # Define a list of messages. When a client sends a "GET", select
    # one randomly and return it.

    MSG_LIST = [
    "1" * 72,
    "2" * 70,
    "3" * 60,
    "4" * 40,
    "5" * 50,
    ]

    MSG_ENCODING = "utf-8"

    def __init__(self):
        self.create_listen_socket()
        self.process_connections_forever()

    def create_listen_socket(self):
        try:
            # Create the TCP server listen socket in the usual way.
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((Server.HOSTNAME, Server.PORT))
            self.socket.listen(Server.BACKLOG)
            print("Listening on port {} ...".format(Server.PORT))
        except Exception as msg:
            print(msg)
            exit()

    def process_connections_forever(self):
        try:
            while True:
                self.connection_handler(self.socket.accept())
        except KeyboardInterrupt:
            print()
        finally:
            self.socket.close()

    def connection_handler(self, client):
        connection, address = client
        print("-" * 72)
        print("Connection received from {}.".format(address))

        # If we have a valid request message ('GET' string), then send
        # an encoded message. Either way, close the client connection.

        recv_result, recv_data = recv_bytes(connection, GET_REQUEST_SIZE)
        if recv_result and recv_data == GET_REQUEST:
            # Pick a random message (file) and send it to the
            # client.
            msg = random.choice(Server.MSG_LIST)
            msg_encoded = msg.encode(Server.MSG_ENCODING)
            connection.sendall(msg_encoded)
            print("Sent message bytes: \n", msg_encoded)
        ########################################################
        # Close the connection after each request is
        # fullfilled or if an invalid request is made.
        ########################################################
        print("Closing connection ...")
        connection.close()

########################################################################
# CLIENT
########################################################################

class Client:

    RECV_SIZE = 1024
    # NUMBER_OF_DOWNLOADS = 2

    def __init__(self):
        self.download_messages()

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

    def download_messages(self):

        # # Download loop to fetch multiple messages from the server.
        # for download_number in range(1, Client.NUMBER_OF_DOWNLOADS+1):

        # Output some status information.
        print("-" * 72)
        # print("Download number: ", download_number)

        ############################################################
        # Create a new TCP connection for each download. We will
        # get a new socket each time.
        ############################################################
        self.get_socket()
        self.connect_to_server()
        print("Connection to ", (Server.HOSTNAME, Server.PORT))

        # Send the download request string to the server.
        self.socket.sendall(GET_REQUEST)

        # recvd_bytes is used to accumulate bytes received over the
        # connection.
        recvd_bytes_total = b""
        
        try:
            ########################################################
            # Read from the connection until the server has closed
            # the other end. Then close this end.
            ########################################################
            while True:
                recvd_bytes = self.socket.recv(Client.RECV_SIZE)
                if len(recvd_bytes) == 0:
                    # The server has completed the download and
                    # has closed the connection. We are done.
                    print(recvd_bytes_total.decode(Server.MSG_ENCODING))
                    print("Closing server connection ... ")
                    self.socket.close()
                    break
                recvd_bytes_total += recvd_bytes
        except KeyboardInterrupt:
            print()
            sys.exit(1)

            # If the socket has been closed by the server, break out
            # and close it on this end.
            # except socket.error as msg:
                # print("msg")
                # break
        
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






