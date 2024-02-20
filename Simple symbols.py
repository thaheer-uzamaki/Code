#simple symbols
def simple_symbols(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    for num in range(len(string)-1):
        if string[0] in letter or string[-1] in letter:
            return False
        elif string[num] in letter:
            if string[num+1]!='+' or string[num-1]!='+':
                return False
    return True
print(simple_symbols(input()))