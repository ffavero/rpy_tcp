import rpy2.robjects as robjects

# Dict of function in this file, so if a function not in list 
# is called, or an existing is not properly called an error rise.
# The format of the dictionary is 'CODE_TO_CALL':'function_name'

FUNCTS = {
 'VERSION': 'version',
 'PLOT1': 'plot1',
 'STRESS':'stress'
}

## Start the various functions:

def version():
   '''
   Dummy function to demostrate function with no argvs
   and out in stdout
   '''
   res = robjects.r('R.version')
   return res

def plot1(ARGVS):
   '''
   Simple plot to demostrate the ARGVS functionality
   '''
   x = [float(i) for i in ARGVS[1].split(',')]
   y = [float(i) for i in ARGVS[2].split(',')]
   robjects.r ('''
      plotfunction <- function(file,x,y) {
       pdf(file)
       plot(x,y)
       dev.off()
      }
   ''')
   robjects.r['plotfunction'](file = ARGVS[0],x = x ,y = y)
   return ARGVS[0] + ' is Ok'


def stress():
   '''
   Plot a big number of point to see the system under stress
   '''
   robjects.r ('''
      pdf(file="plot1.pdf")
      plot(x=c(1:10000000),y=c(1:10000000))
      dev.off()
   ''')
   return 'Done\n' 
