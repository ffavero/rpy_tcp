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
