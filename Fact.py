#first factorial
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
print(first_factorial(int(input())))

#first factorial(reverse both and append semi colon)
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    token='abcd'
    res1=res[::-1]
    token1=token[::-1]
    return f'{res1}:{token1}'
print(process(int(input())))

#first factorial(replace 4th character with '-')
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    token='abcdefghi'
    res=str(first_factorial(num))+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(process(int(input())))

#first factorial(replace 3rd character with 'x')
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    token='abcdefgh'
    res=str(first_factorial(num))
    result=res+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(process(int(input())))

#first factorial(add '--' before and after char,if char in token)
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    result=''
    token='abc2nj0'
    for char in res:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(process(int(input())))

#first factorial(alternate output)
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    token='abcdefg'
    result=''
    i,j=0,0
    while i<len(res) and j<len(token):
        result+=res[i]+token[j]
        i+=1
        j+=1
    result+=res[i:]+token[j:]
    return result
print(process(int(input())))

#first factorial(add '-' after every character)
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    fin =""
    count=0
    for i in res:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]  
print(process(int(input())))

#first factorial(if char in token, replace with '-')
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    token='tgy2huj'
    result=[]
    for i in res:
        if i in token:
            result.append('_')
        else:
            result.append(i)
    return ''.join(result)
print(process(int(input())))

#first factorial(if char in token,remove those characters,if all the characters are removed then return empty)
def first_factorial(num):
    if num==0:
        return 1
    return first_factorial(num-1)*num
def process(num):
    res=str(first_factorial(num))
    token='5oq2nca479'
    result=''
    for i in str(res):
        if i.lower() not in token.lower():
            result+=i
    if result:
        print(result)
    else:
        print('EMPTY')
process(int(input()))