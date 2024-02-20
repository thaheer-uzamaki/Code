#first reverse
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    return character
print(first_reverse(input()))

#first_reverse(reverse both and append semi colon)
token='abcd'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=token[::-1]
    return f'{character}:{res}'
print(first_reverse(input()))

#first_factorial(replace 4th character with '-')
token='abcdefgh'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=character+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(first_reverse(input()))

#first_reverse(replace 3rd character with 'x')
token='abcdefg'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=character+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(first_reverse(input()))

#first_reverse(add '--' before and after char,if char in token)
token='abcdefg'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=''
    for chara in character:
        if chara in token:
            res+=f'--{chara}--'
        else:
            res+=chara
    return res
print(first_reverse(input()))

#first_reverse(alternate output)
token='pqrs'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=''
    i,j=0,0
    while i<len(character) and j<len(token):
        res+=character[i]+token[j]
        i+=1
        j+=1
    res+=character[i:]+token[j:]
    return res
print(first_reverse(input()))

#first_reverse(add '-' after every character)
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    fin =""
    count=0
    for i in character:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]    
print(first_reverse(input()))

#first_reverse(if char in token, replace with '-')
token='abdef'
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    res=[]
    for i in character:
        if i in token:
            res.append('_')
        else:
            res.append(i)
    return ''.join(res)
print(first_reverse(input()))

#first reverse(if char in token,remove those characters,if all the characters are removed then return empty)
def first_reverse(string):
    character=''
    for char in string[::-1]:
        character+=char
    token='5oq2nca479'
    res=''
    for i in character:
        if i.lower() not in token.lower():
            res+=i
    if res:
        print(res) 
    else:
        print('EMPTY')
first_reverse(input())