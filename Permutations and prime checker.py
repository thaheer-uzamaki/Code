import itertools
def permutation(num):
    p=[int(''.join(i)) for i in itertools.permutations (str(num))]
    p.sort()
    ins=p.index(num)
    try:
        if p[ins+1]>num:
            return p[ins+1]
        else:
            return -1
    except IndexError:
        return -1
print(permutation(123))
132
#prime checker
from itertools import permutations
import math
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
def prime_checker(nums):
    num_str=str(nums)
    perms=permutations(num_str)
    for perm in perms:
        perm_str=int(''.join(perm))
        if is_prime(perm_str):
            return 1
    return 0
print(prime_checker(910))