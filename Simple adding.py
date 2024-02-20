#simple adding
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    return total
print(simple_adding(int(input())))

#simple adding(reverse both and append semi colon)
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    res1=str(total)
    token='abcd'
    token1=token[::-1]
    res=res1[::-1]
    return f'{res}:{token1}'
print(simple_adding(int(input())))

#simple adding(replace 4th character with '-')
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='abcdefg'
    res=str(total)+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(simple_adding(int(input())))

#simple adding(replace 3rd character with 'x')
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='abcdefg'
    res=str(total)+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(simple_adding(int(input())))

#simple adding(add '--' before and after the character, if character in token)
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='fgy5huj'
    res=''
    for i in str(total):
        if i in token:
            res+=f'--{i}--'
        else:
            res+=i
    return res
print(simple_adding(int(input())))

#simple adding(alternate output)
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='abc'
    res=str(total)
    result=''
    i,j=0,0
    while i<len(res) and j<len(token):
        result+=res[i]+token[j]
        i+=1
        j+=1
    result+=res[i:]+token[j:]
    return result
print(simple_adding(int(input())))

#simple adding(add '-' after every character)
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    fin =""
    count=0
    for i in str(total):
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(simple_adding(int(input())))

#simple adding(if char in token, replace with '-')
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='rft5gyh'
    res=[]
    for char in str(total):
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(simple_adding(int(input())))

#simple adding(if char in token,remove those characters,if all the characters are removed then return empty)
def simple_adding(num):
    total=0
    for num in range(num+1):
        total+=num
    token='gthy5jui'
    res=''
    for char in str(total):
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
simple_adding(int(input()))