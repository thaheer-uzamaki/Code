#letter capitalization
def letter_capitalization(string):
    res=string.title()
    return res
print(letter_capitalization(input()))

#letter capitalization(reverse both and append semi colon)
def letter_capitalization(string):
    res=string.title()
    res1=res[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(letter_capitalization(input()))

#letter capitalization(replace 4th character with '-')
def letter_capitalization(string):
    res=string.title()
    token='abcd'
    result=res+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(letter_capitalization(input()))

#letter capitalization(replace 3rd character with 'x')
def letter_capitalization(string):
    res=string.title()
    token='abcd'
    result=res+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(letter_capitalization(input()))

#letter capitalization(add '--' before and after char,if char in token)
def letter_capitalization(string):
    res=string.title()
    token='abcd'
    result=''
    for char in res:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(letter_capitalization(input()))

#letter capitalization(alternate output)
def letter_capitalization(string):
    res=string.title()
    token='abcd'
    result=''
    i,j=0,0
    while i<len(res) and j<len(token):
        result+=res[i]+token[j]
        i+=1
        j+=1
    result+=res[i:]+token[j:]
    return result
print(letter_capitalization(input()))

#letter capitalization(add '-' after every character)
def letter_capitalization(string):
    res=string.title()
    fin =""
    count=0
    for i in res:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(letter_capitalization(input()))

#letter capitalization(if char in token, replace with '-')
def letter_capitalization(string):
    res=string.title()
    token='abcd'
    result=[]
    for char in res:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(letter_capitalization(input()))

#letter capitalization(if char in token,remove those characters,if all the characters are removed then return empty)
def letter_capitalization(string):
    res=string.title()
    token='abcdt'
    result=''
    for char in res:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
letter_capitalization(input())