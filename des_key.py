import string
import random
def rand_str(num):
    if num <= 8:
        N = 8 + num
    else:  
        N = num
    
    res = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = N))
    return(res)

