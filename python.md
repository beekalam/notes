# network programming
## intro
### machine name and IP

```python
import socket
host_name = socket.gethostname()
socket.gethostbyname(host_name)
```
### retrieving a remote machine's IP address
```python
import socket

def get_remote_machine_info():
  remote_host='www.python.org'
  try:
    print "IP address: %s" % socket.gethostbyname(remote_host)
  except socket.error, err_msg:
    print "%s: %s" % (remote_host, err_msg)
```

### converting an IPV4 address to different formats

```python
import socket
from binascii import hexlify

def convert_ip4_address():
  for ip in ['127.0.0.1', '192.168.0.1']:
    packed_ip_addr= socket.inet_aton(ip_addr)
    unpacked_ip_addr= socket.inet_ntoa(packed_ip_addr)
    print "IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)
```


### Finding a service name, given the port and protocol
```python
import socket

def find_service_name():
  protocolname = 'tcp'
  for port in [80, 25]:
    print "Port: %s => service name: %s" % (port, socket.getsrvbyport(port, protocolname))
```

### converting integers to and from host to network byte order
```python
import socket
def convert_integer():
  data = 1234
  # 32 bit
  print "Original : %s => Long host byte order: %s, Network byte order: %s " % (data. socket.ntohl(data), socket.htonl(data))
  # 16 bit
  print "Original : %s => Short host byte order: %s, Network b yte order: %s " % (data, socket.ntohs(data), socket.htons(data))
```

### setting and getting the default socket timeout
```python
import socket
def test_socket_timeout():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print "Default socket timeout: %s" % s.gettimeout()
  s.settimeout(100)
  print "current socket timeout: %s" % s.gettimeout()
```

### handling socket errors gracefully
```python
import sys
import socket
import argparse

def main():
  # setup argument parsing
  parser = argparse.ArgumentParser(description='Socket error examples')
  parser.add_argument('--host', action="store", dest="host", required = False)
  parser.add_argument('--port', action="store", dest="port", required = False)
  parser.add_argument('--file', action="store", dest="file", required= False)
  given_args = parser.parse_args()
  host = given_args.host
  port = given_args.port
  filename = given_args.file
  
  #First try-except block -- create socket
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error, e:
    print "Error creating socket: %s" % e
    sys.exit(1)

  # second try-except block -- connect to given host/port
  try:
     s.connect((host,port))
  except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
  except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)
  # third try-except block -- sending data
  try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n"  % filename)
  except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)
  while 1:
    #Fourth try-except block -- waiting to receive data from remote host
    try:
      buf = s.recv(2048)
    except socket.error, e:
      print "Error receiving data: %s" % e
      sys.exit(1)
    if not len(buf):
      break
    # write the received data
    sys.stdout.wirte(buf)
    
if __name__ == '__main__':
  main()
```

### modifying socket's send/receive buffer size
The default socket buffer size may not be suitable in many circumstance. In such
circumstances, youc an change the default socket buffer size to a more suitable value.

```python
import socket
SEND_BUF_SIZE = 4094
REC_BUF_SIZE = 4096
def modify_buff_size():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  #Get the size of the socket's send buffer
  bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  print "Buffer size [Before]:%d" % bufsize
  
  sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
  sock.setsockopt( socket.SOL_SOCKET, socket.SO_SNDBUF,SEND_BUF_SIZE)
  sock.setsockopt( socket.SOL_SOCKET, socket.SO_RECVBUF, RECV_BUF_SIZE)
  bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
  print "Buffer size [After]:%d" %bufsize
```

### changing a socket to the blocking/nonblocking mode
By default, TCP sockets are placed in a blocking mode. This means the control is not returned
to your program until some specific operation is complete. For example, if you call the
connect() API, the connection blocks your program until the operation is complete. On many
occasions, you don't want to keep your program waiting forever, either for a response from the
server or for any error to stop the operation. For example, when you write a web browser client
that connects to a web server, you should consider a stop functionality that can cancel the
connection process in the middle of this operation. This can be achieved by placing the socket
in the non-blocking mode.

```python
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications
import socket
def test_socket_modes():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(1)
s.settimeout(0.5)
s.bind(("127.0.0.1", 0))
socket_address = s.getsockname()
print "Trivial Server launched on socket: %s" %str(socket_address)
while(1):
s.listen(1)
if __name__ == '__main__':
test_socket_modes()
```
### Reusing socket addresses

You want to run a socket server always on a specific port even after it is closed intentionally or
unexpectedly. This is useful in some cases where your client program always connects to that
specific server port. So, you don't need to change the server port.
How to do it...

If you run a Python socket server on a specific port and try to rerun it after closing it once, you
won't be able to use the same port. It will usually throw an error like the following command:

```python
Traceback (most recent call last):
File "1_10_reuse_socket_address.py", line 40, in <module>
reuse_socket_addr()
File "1_10_reuse_socket_address.py", line 25, in reuse_socket_addr
srv.bind( ('', local_port) )
File "<string>", line 1, in bind
socket.error: [Errno 98] Address already in use
```

The remedy to this problem is to enable the socket reuse option, SO_REUSEADDR .
After creating a socket object, we can query the state of address reuse, say an old state. Then,
we call the setsockopt() method to alter the value of its address reuse state. Then, we
follow the usual steps of binding to an address and listening for incoming client connections.
In this example, we catch the KeyboardInterrupt exception so that if you issue Ctrl + C,
then the Python script gets terminated without showing any exception message.
Listing 1.10 shows how to reuse socket addresses as follows:

```python
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications
import socket
import sys
def reuse_socket_addr():
sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
# Get the old state of the SO_REUSEADDR option
old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR
)
print "Old sock state: %s" %old_state
# Enable the SO_REUSEADDR option
sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_
REUSEADDR )
print "New sock state: %s" %new_state
local_port = 8282
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind( ('', local_port) )
srv.listen(1)
print ("Listening on port: %s " %local_port)
while True:
try:
connection, addr = srv.accept()
print 'Connected by %s:%s' % (addr[0], addr[1])
except KeyboardInterrupt:
break
except socket.error, msg:
print '%s' % (msg,)
if __name__ == '__main__':
reuse_socket_e addr()
```

The output from this recipe will be similar to the following command:
$ python 1_10_reuse_socket_address.py
Old sock state: 0
New sock state: 1
Listening on port: 8282

### Printing the current time from the internet time server
Here, the client/server conversation will be done using __NETWORK TIME PROTOCOL__
if ntplib is not installed on your machine, you can get it from PyPI:
`$ pip install ntplib`

```python
import ntplib
from time import ctime

def print_time():
  ntp_client = ntplib.NTPClient()
  response = ntp_client.request('pool.ntp.org')
  print ctime(response.tx_time)

if __name__=='__main__':
  print_time()
```


### writing sntp client
Unlike the previous recipe, sometimes, you don't need to get the precise time from the NTP
server. You can use a simpler version of NTP called simple network time protocol.

How to do it...
Let us create a plain SNTP client without using any third-party library.
Let us first define two constants: NTP_SERVER and TIME1970. NTP_SERVER is the server
address to which our client will connect, and TIME1970 is the reference time on January 1,
1970 (also called Epoch). You may find the value of the Epoch time or convert to the Epoch
time at http://www.epochconverter.com/ . The actual client creates a UDP socket
( SOCK_DGRAM ) to connect to the server following the UDP protocol. The client then needs to
send the SNTP protocol data ( '\x1b' + 47 * '\0' ) in a packet. Our UDP client sends and
receives data using the sendto() and recvfrom() methods.
When the server returns the time information in a packed array, the client needs a specialized
struct module to unpack the data. The only interesting data is located in the 11th element
of the array. Finally, we need to subtract the reference value, TIME1970 , from the unpacked
value to get the actual current time.

Listing 1.11 shows how to write an SNTP client as follows:

```python
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications
import socket
import struct
import sys
import time
NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L
def sntp_client():
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = '\x1b' + 47 * '\0'
client.sendto(data, (NTP_SERVER, 123))
data, address = client.recvfrom( 1024 )
if data:
print 'Response received from:', address
t = struct.unpack( '!12I', data )[10]
t -= TIME1970
print '\tTime=%s' % time.ctime(t)
if __name__ == '__main__':
sntp_client()
```

This recipe prints the current time from the Internet time server received with the SNTP
protocol as follows:

$ python 1_12_sntp_client.py
Response received from: ('87.117.251.2', 123)
Time=Tue Feb 25 14:49:38 2014

How it works...
This SNTP client creates a socket connection and sends the protocol data. After receiving the
response from the NTP server (in this case, 0.uk.pool.ntp.org ), it unpacks the data with
struct . Finally, it subtracts the reference time, which is January 1, 1970, and prints the time
using the ctime() built-in method in the Python time module.


### Writing a simple echo client/server application
fter testing with basic socket APIs in Python, let us create a socket server and client now.
Here, you will have the chance to utilize your basic knowledge gained in the previous recipes.
How to do it...

In this example, a server will echo whatever it receives from the client. We will use the Python
argparse module to specify the TCP port from a command line. Both the server and client
script will take this argument.

First, we create the server. We start by creating a TCP socket object. Then, we set the reuse
address so that we can run the server as many times as we need. We bind the socket to the
given port on our local machine. In the listening stage, we make sure we listen to multiple
clients in a queue using the backlog argument to the listen() method. Finally, we wait for
the client to be connected and send some data to the server. When the data is received, the
server echoes back the data to the client.
Listing 1.13a shows how to write a simple echo client/server application as follows:

```python
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter – 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.
import socket
import sys
import argparse
host = 'localhost'
data_payload = 2048
backlog = 5
def echo_server(port):
  """ A simple echo server """
  # Create a TCP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Enable reuse address/port
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # Bind the socket to the port
  server_address = (host, port)
  print "Starting up echo server on %s port %s" % server_address
  sock.bind(server_address)
  # Listen to clients, backlog argument specifies the max no. of
  queued connections
  sock.listen(backlog)
  while True:
    print "Waiting to receive message from client"
    client, address = sock.accept()
    data = client.recv(data_payload)
    if data:
      print "Data: %s" %data
      client.send(data)
      print "sent %s bytes back to %s" % (data, address)
  # end connection
  client.close()

if __name__ == '__main__':
parser = argparse.ArgumentParser(description='Socket Server Example')
parser.add_argument('--port', action="store", dest="port",
type=int, required=True)
given_args = parser.parse_args()
port = given_args.port
echo_server(port)
```

On the client-side code, we create a client socket using the port argument and connect to the
server. Then, the client sends the message, Test message. This will be echoed to
the server, and the client immediately receives the message back in a few segments. Here,
two try-except blocks are constructed to catch any exception during this interactive session.
Listing 1-13b shows the echo client as follows:

```python
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter – 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications.
import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
  """ A simple echo client """
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Connect the socket to the server
  server_address = (host, port)
  print "Connecting to %s port %s" % server_address
  sock.connect(server_address)
  # Send data
  try:
    # Send data
    message = "Test message. This will be echoed"
    print "Sending %s" % message
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
      data = sock.recv(16)
      amount_received += len(data)
      print "Received: %s" % data
  except socket.errno, e:
    print "Socket error: %s" %str(e)
  except Exception, e:
    print "Other exception: %s" %str(e)
  finally:
    print "Closing connection to the server"
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
# ##   port = given_args.port
  echo_client(port)
```


## Multiplexing Socket I/O for better performance
### Using ForkingMixIn in your socket server applications
You have decided to write an asynchronous Python socket server application. The server will not block in processing a client request. So the server needs a mechanism to deal with each client independently.

Python 2.7 version's SocketServer class comes with two utility classes: ForkingMixIn and ThreadingMixIn . 
The ForkingMixin class will spawn a new process for each client request. This class is discussed in this section. 
The ThreadingMixIn class will be discussed in the next section. For more information, you can refer to the Python documentation at
http://docs.python.org/2/library/socketserver.html .

__How to do it...__
Let us rewrite our echo server, previously described in Chapter 1, Sockets, IPv4, and Simple Client/Server Programming. We can utilize the subclasses of the SocketServer class family.

It has ready-made TCP, UDP, and other protocol servers. We can create a ForkingServer class inherited from TCPServer and ForkingMixin . The former parent will enable our ForkingServer 
class to do all the necessary server operations that we did manually before,such as creating a socket, 
binding to an address, and listening for incoming connections. Our server also needs to inherit from ForkingMixin to handle clients asynchronously.
The ForkingServer class also needs to set up a request handler that dictates 

__how to__
handle a client request. Here our server will echo back the text string received from the client. Our request handler class ForkingServerRequestHandler 
is inherited from the BaseRequestHandler provided with the SocketServer library.

We can code the client of our echo server, ForkingClient , in an object-oriented fashion.

In Python, the constructor method of a class is called __init__() . By convention, it takes a self-argument to attach attributes or properties of that particular class.
The ForkingClient echo server will be initialized at __init__() and sends the message to the server at the run() method respectively.
If you are not familiar with object-oriented programming (OOP) at all, it might be helpful to review the basic concepts of OOP while attempting to grasp this recipe.

In order to test our ForkingServer class, we can launch multiple echo clients and see how the server responds back to the clients.


