#longest word
import re
def longest_word(string):
    res=re.findall('\w+',string)
    return max(res,key=len)
print(longest_word(input()))

#longest word(reverse both and append semi colon)
import re
def longest_word(string):
    words=re.findall('\w+',string)
    result=max(words,key=len)
    token='abcdefg'
    result1=result[::-1]
    token1=token[::-1]
    return f'{result1}:{token1}'
print(longest_word(input()))

#longest word(replace 4th character with '-')
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='abcdefgh'
    result=res+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(longest_word(input()))

#longest word(replace 3rd character with 'x')
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='abcdefgh'
    result=res+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(longest_word(input()))

#longest word(add '--' before and after the character, if character in token)
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='abcdef'
    result=''
    for char in res:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(longest_word(input()))

#longest word(alternate output)
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='abcdefg'
    i,j=0,0
    result=''
    while i<len(res) and j<len(token):
        result+=res[i]+token[j]
        i+=1
        j+=1
    result+=res[i:]+token[j:]
    return result
print(longest_word(input()))

#longest word(add '-' after every character)
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    fin =""
    count=0
    for i in res:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1] 
print(longest_word(input()))

#longest word(if char in token, replace with '-')
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='abcdef'
    result=[]
    for char in res:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(longest_word(input()))

#longest word(if char in token,remove those characters,if all the characters are removed then return empty)
import re
def longest_word(string):
    words=re.findall('\w+',string)
    res=max(words,key=len)
    token='pqrst'
    result=''
    for char in res:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
longest_word(input())