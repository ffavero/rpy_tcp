import SocketServer
import sys
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
      # Decoding the JSON coming from the client
      CODE = self.data['function']
      if self.data['argvs']:
         print "With args"
         ARGS  = self.data['argvs']

      # evaluate the given function
         try:
            results = getattr(functions, funcs[CODE])(ARGS)
         except:
            self.wfile.write('System error, sorry')
      else:
         print "No args"
         try:
            results = getattr(functions, funcs[CODE])()  
         except:
            self.wfile.write('System error, sorry')
      if str(results):
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
