#word count
def word_count(string):
    word=string.split()
    return len(word)
print(word_count(input()))

#word count(reverse both and append semi colon)
def word_count(string):
    word=string.split()
    res=len(word)
    res1=str(res)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(word_count(input()))

#word count(replace 4th character with '-')
def word_count(string):
    word=string.split()
    res=len(word)
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(word_count(input()))

#word count(replace 3rd character with 'x')
def word_count(string):
    word=string.split()
    res=len(word)
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(word_count(input()))

#word count(add '--' before and after char,if char in token)
def word_count(string):
    word=string.split()
    res=len(word)
    token='ab4cd'
    result=''
    for char in str(res):
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(word_count(input()))

#word count(alternate output)
def word_count(string):
    word=string.split()
    res=len(word)
    res1=str(res)
    token='ab4cd'
    result=''
    i,j=0,0
    while i<len(res1) and j<len(token):
        result+=res1[i]+token[j]
        i+=1
        j+=1
    result+=res1[i:]+token[j:]
    return result
print(word_count(input()))

#word count(add '-' after every character)
def word_count(string):
    word=string.split()
    res=len(word)
    res1=str(res)
    fin =""
    count=0
    for i in str(res):
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(word_count(input()))

#word count(if char in token, replace with '-')
def word_count(string):
    word=string.split()
    res=len(word)
    res1=str(res)
    token='ab2cdef'
    result=[]
    for char in res1:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(word_count(input()))

#word count(if char in token,remove those characters,if all the characters are removed then return empty)
def word_count(string):
    word=string.split()
    res=len(word)
    res1=str(res)
    token='ab2c4def'
    result=''
    for char in res1:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
word_count(input())