#!/usr/bin/env python

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0 # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkedClient():
    """ A client to test forking server"""
    def __init__(self, ip, port):
        # create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to the server
        self.sock.connect((ip, port))

    def run(self):
        """ client playing with the servr"""
        # send the data to server
        current_process_id = os.getpid()
        print 'PID %s sending echo message to the server : "%s"' % (current_process_id, ECHO_MSG)
        sent_data_length = self.sock.send(ECHO_MSG)
        print "sent: %d characters , so far ... " % sent_data_length

        #display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID %s received: %s" % (current_process_id, response[5:])

    def shutdown(self):
        """ clean up the client socket"""
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s:%s' % (current_process_id, data)
        print "Server sending response [current_process_id: data]=[%s]" % response
        self.request.send(response)
        return

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """ Nothing to add here, inherited everything necessary from parentsf"""
    pass

def main():
    #Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip,port = server.server_address # Retrieve the port number
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True) # dont' hang on exit
    server_thread.start()
    print 'server loop running PID: %s' % os.getpid()

    #Launch the clients
    client1= ForkedClient(ip, port)
    client1.run()

    client2 = ForkedClient(ip, port)
    client2.run()

    # clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == "__main__":
    main()
