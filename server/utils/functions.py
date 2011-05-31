import rpy2.robjects as robjects

# Dict of function in this file, so if a function not in list 
# is called, or an existing is not properly called an error rise.
# The format of the dictionary is 'CODE_TO_CALL':'function_name'

FUNCTS = {
 'VERSION': 'version',
 'PLOT1': 'plot1'
}

## Start the various functions:

def version():
   res = robjects.r('R.version')
   return res

def plot1(ARGVS):
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
