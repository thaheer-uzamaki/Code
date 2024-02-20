#sum of largest four
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    return b
print(largest([0, 0, 2, 3, 7, 1]))
13
#sum of largest four(reverse both and append semi colon)
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    res1=res[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(largest([1, 1, 1, -5]  ))
2-:dcba
#sum of largest four(replace 4th character with '-')
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    token='abcd'
    res=str(b)+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(largest([1,1,1,-5]))
    
-2a-cd
#sum of largest four(replace 3rd character with 'x')
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    token='abcd'
    res=str(b)+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(largest([1,1,1,-5]))
    
-2xbcx
#sum of largest four(add '--' before and after char,if char in token)
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    token='ab-cd'
    res1=''
    for char in res:
        if char in token:
            res1+=f'--{char}--'
        else:
            res1+=char
    return res1
print(largest([1,1,1,-5]))
-----2
#sum of largest four(alternate output)
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    token='abcd'
    res1=''
    i,j=0,0
    while i<len(res) and j<len(token):
        res1+=res[i]+token[j]
        i+=1
        j+=1
    res1+=res[i:]+token[j:]
    return res1
print(largest([1,1,1,-5]))
-a2bcd
#sum of largest four(add '-' after every character)
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    fin =""
    count=0
    for i in res:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(largest([1,1,1,-5]))
--2
#sum of largest four(if char in token, replace with '-')
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    token='abc-d'
    res1=[]
    for char in res:
        if char in token:
            res1.append('_')
        else:
            res1.append(char)
    return ''.join(res1)
print(largest([1,1,1,-5]))
_2
#sum of largest four(if char in token,remove those characters,if all the characters are removed then return empty)
def largest(arr):
    a=sorted(arr,reverse=True)
    b=sum(a[:4])
    res=str(b)
    token='abc-d'
    res1=''
    for char in res:
        if char.lower() not in token.lower():
            res1+=char
    if res1:
        print(res1)
    else:
        print('EMPTY')
largest([1,1,1,-5])