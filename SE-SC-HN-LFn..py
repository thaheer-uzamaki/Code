#simple evens
def simple_even(num):
    res=num
    for digit in str(num):
        if int(digit)%2!=0:
            return False
    return True
print(simple_even(int(input())))
20864646452    
False
#Happy number
def happy_number(num):
    seen_number=set()
    while num!=1 and num not in seen_number:
        seen_number.add(num)
        num=sum(int(digit)**2 for digit in str(num))
    return num==1
print(happy_number(int(input())))
101
False
#swap case
def swap_case(string):
    result=string.swapcase()
    return result
print(swap_case(input()))
HeLLo
hEllO
#sum of largest four
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    return b
print(largest([0, 0, 2, 3, 7, 1]))