#alphabet soup
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    return b
print(alphabet_soup(input()))

#alphabet soup(reverse both and append semi colon)
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    b1=b[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{b1}:{token1}'
print(alphabet_soup(input()))

#alphabet soup(replace 4th character with '-')
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcd'
    result=b+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(alphabet_soup(input()))

#alphabet soup(replace 3rd character with 'x')
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcd'
    result=b+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(alphabet_soup(input()))

#alphabet soup(add '--' before and after char,if char in token)
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcde'
    result=''
    for char in b:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(alphabet_soup(input()))

#alphabet soup(alternate output)
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcde'
    result=''
    i,j=0,0
    while i<len(b) and j<len(token):
        result+=b[i]+token[j]
        i+=1
        j+=1
    result+=b[i:]+token[j:]
    return result
print(alphabet_soup(input()))

#alphabet soup(add '-' after every character)
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    fin =""
    count=0
    for i in b:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(alphabet_soup(input()))

#alphabet soup(if char in token, replace with '-')
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcde'
    result=[]
    for char in b:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(alphabet_soup(input()))

#alphabet soup(if char in token,remove those characters,if all the characters are removed then return empty)
def alphabet_soup(string):
    res=[]
    for char in string.lower():
        res.append(char)
    a=sorted(res)
    b=''.join(a)
    token='abcdehlo'
    result=''
    for char in b:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
alphabet_soup(input())