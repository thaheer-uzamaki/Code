#plus minus
def plus_minus(num):
    digits=list(map(int,str(num)))
    n=len(digits)
    for i in range(1<<n):
        s=sum(digits[j] if ((i >> j) & 1) else -digits[j] for j in range(n))
        if s == 0:
            return ''.join(['+' if ((i >> j) & 1) else '-' for j in range(1, n)])
    return "not possible"
print(plus_minus(input()))