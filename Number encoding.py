#number encoding
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    return b
print(number_encoding('af5c a#!'))
1653 1#!
#number encoding(reverse both and append semi colon)
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    b1=b[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{b1}:{token1}'
print(number_encoding('af5c a#!'))
!#1 3561:dcba
#number_encoding(replace 4th character with '-')
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='abcd'
    res=b+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(number_encoding('af5c a#!'))
165- 1#-abc-
#number encoding(replace 3rd character with 'x')
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='abcd'
    res=b+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(number_encoding('af5c a#!'))
16x3 x#!xbcx
#number encoding(add '--' before and after char,if char in token)
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='ab5cd'
    res=''
    for char in b:
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(number_encoding('af5c a#!'))
16--5--3 1#!
#number encoding(alternate output)
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='ab5cd'
    res=''
    i,j=0,0
    while i<len(b) and j<len(token):
        res+=b[i]+token[j]
        i+=1
        j+=1
    res+=b[i:]+token[j:]
    return res
print(number_encoding('af5c a#!'))
1a6b553c d1#!
#number encoding(add '-' after every character)
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    fin =""
    count=0
    for i in b:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(number_encoding('af5c a#!'))
1-6-5-3- -1-#-!
#number encoding(if char in token, replace with '-')
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='ab5cd'
    res=[]
    for char in b:
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(number_encoding('af5c a#!'))
16_3 1#!
#number encoding(if char in token,remove those characters,if all the characters are removed then return empty)
def number_encoding(string):
    a=string.lower()
    b=''
    for char in a:
        if char.isalpha():
            b+=str(ord(char)-ord('a')+1)
        else:
            b+=char
    token='ab5cd'
    res=''
    for char in b:
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
number_encoding('af5c a#!')