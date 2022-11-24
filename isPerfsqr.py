#!/usr/bin/python3

import math
def isSqr(x):    
    if(x >= 0):
        sr = int(math.sqrt(x))
        # sqrt function returns floating value so we have to convert it into integer
        #return boolean T/F
        return ((sr*sr) == x)
    return false
