from __future__ import with_statement
import json as simplejson
import socket
import sys

HOST, PORT = sys.argv[1].split(":")
PORT = int(PORT)
function = sys.argv[2]
type     = sys.argv[3] 
argvs    = sys.argv[4:]
data = simplejson.dumps({'function':function,'type':type,'argvs':argvs})

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST, PORT))
sock.send(data + "\n")

# Receive data from the server and shut down

if type != 'stdout':
   filesize = int(sock.recv(1024))
   received = ''
   while len(received) < filesize:
      received += sock.recv( filesize - len(received) )
   sock.close()
else:
   received = sock.recv(1024)
print "Sent:     %s" % data
if type != 'stdout':
   TYPE,FILE = type.split(':')
   with open(FILE, "w") as f:  
      f.write(received)
   print  'File saved'

else:
   print "Received:   %s" % received
