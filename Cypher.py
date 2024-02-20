#caesar cipher
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    return result
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
ecguct ekrjgt
#caesar cipher(reverse both and append semi colon)
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    res=result[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res}:{token1}'
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
tgjrke tcugce:dcba
#caesar cipher(replace 4th character with '-')
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='pqrst'
    res=result+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
ecg-ct -krj-tpq-st
#caesar cipher(replace 3rd character with 'x')
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='pqrst'
    res=result+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesarcipher
2
ecxucxekxjgxpqxst
#caesar cipher(add '--' before and after char,if char in token)
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='pqrst'
    res=''
    for char in result:
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
ecguc--t-- ek--r--jg--t--
#caesar cipher(alternate output)
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='pqrst'
    res=''
    i,j=0,0
    while i<len(result) and j<len(token):
        res+=result[i]+token[j]
        i+=1
        j+=1
    res+=result[i:]+token[j:]
    return res
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
epcqgrusctt ekrjgt
#caesar cipher(add '-' after every character)
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    fin =""
    count=0
    for i in result:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
e-c-g-u-c-t- -e-k-r-j-g-t
#caesar cipher(if char in token, replace with '-')
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='abcd'
    res=[]
    for char in result:
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
string=input()
num=int(input())
print(caesar_cipher(string,num))
caesar cipher
2
e_gu_t ekrjgt
#caesar cipher(if char in token,remove those characters,if all the characters are removed then return empty)
def caesar_cipher(string,num):
    l_letter='abcdefghijklmnopqrstuvwxyz'
    u_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    for char in string:
        if char not in l_letter and char not in u_letter:
            result+=char
        elif char.isupper():
            index=u_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=u_letter[new_index]
        else:
            index=l_letter.index(char)
            new_index=(index+num)%25
            if (index+num)>25:
                new_index-=1
            result+=l_letter[new_index]
    token='abcd'
    res=''
    for char in result:
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
string=input()
num=int(input())
caesar_cipher(string,num)