import SocketServer
import sys
import os
## To be changed in version <2.6 in inport simplejson
import json as simplejson
from utils import functions

class MyTCPHandler(SocketServer.StreamRequestHandler):

   def handle(self):
      # self.rfile is a file-like object created by the handler;
      # we can now use e.g. readline() instead of raw recv() calls
      # Read the data and re-encode it in JSON
      self.data = simplejson.loads(self.rfile.readline().strip())
      # verbose server
      print "%s wrote:" % self.client_address[0]
      print self.data
      results = ''

      # Import the Dict of the functions in utils
      funcs = functions.FUNCTS
      # Take the information from the JSON coming from the client
      CODE = self.data['function']
      if self.data['type'] == 'stdout':
         TYPE = self.data['type']
      else:
         try:
            TYPE, FILE = self.data['type'].split(':')
         except:
            print 'Misformat request type. results redirect in stdout'
      if self.data['argvs']:
         print "With args"
         ARGVS = self.data['argvs']
         ARGVS = ARGVS[0].split(";")
      # evaluate the given function
         try:
            results = getattr(functions, funcs[CODE])(ARGVS)
         except:
            self.wfile.write('System error, sorry')
      else:
         print "No args"
         try:
            results = getattr(functions, funcs[CODE])()  
         except:
            self.wfile.write('System error, sorry')
      if str(results):
         if FILE:
            filesize = os.path.getsize(FILE)
            self.wfile.write(str(filesize))
            results = ''
            with open(FILE, "rb") as f:
               byte = f.read(1)
               while byte != "":
                  results += byte
                  byte = f.read(1)
            self.wfile.write(str(results))
         else:
            self.wfile.write(str(results))

if __name__ == "__main__":
   HOST, PORT = "localhost", int(sys.argv[1])

   # Create the server, binding to localhost on the pssed port
   server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
   # To create a threaded server:
   # server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
   # Activate the server; this will keep running until you
   # interrupt the program with Ctrl-C
   server.serve_forever()
