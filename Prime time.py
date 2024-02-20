#prime time
import math
def prime_time(num):
    if num<=1:
        return False
    elif num==2 or num==3:
        return True
    else:
        if num%2==0:
            return False
        else:
            for pf in range(3,int(math.sqrt(num)+1),2):
                if num%pf==0:
                    return False
    return True
print(prime_time(int(input())))