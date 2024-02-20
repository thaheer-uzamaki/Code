#dash insert
def dash_insert(string):
    result=''
    for i in range(len(string)-1):
        result+=string[i]
        if is_even(int(string[i])) and is_even(int(string[i+1])):
            result+='*'
        elif is_odd(int(string[i])) and is_odd(int(string[i+1])):
            result+='-'
    result+=string[-1]
    return result
def is_even(num):
    return num%2==0
def is_odd(num):
    return num%2!=0
print(dash_insert('4546793'))