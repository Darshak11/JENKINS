import math
def isSqr(number):    
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return 1
    return 0