#prime mover
import math
def prime_mover(num):
    primes=get_prime()
    return primes[num-1]
def get_prime():
    primes=[2]
    num=3
    while num<=10000:
        if is_prime(num):
            primes.append(num)
        num+=2
    return primes
def is_prime(num):
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
print(prime_mover(int(input())))