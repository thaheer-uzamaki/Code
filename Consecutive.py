#consecutive
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    return len(length)
print(consecutive([4,8,6]))
2
#consecutive(reverse both and append semi colon)
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    res1=str(res)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(consecutive([2,16,6]))
21:dcba
#consecutive(replace 4th character with '-')
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    token='abcd'
    res1=str(res)+token
    res_list=list(res1)
    for i in range(3,len(res1),4):
        res_list[i]='-'
    res1=''.join(res_list)
    return res1
print(consecutive([2,16,6]))
12a-cd
#consecutive(replace 3rd character with 'x')
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    token='abcd'
    res1=str(res)+token
    res_list=list(res1)
    for i in range(2,len(res1),3):
        res_list[i]='x'
    res1=''.join(res_list)
    return res1
print(consecutive([2,16,6]))
12xbcx
#consecutive(add '--' before and after char,if char in token)
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    token='abc2d'
    result=''
    for char in str(res):
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(consecutive([2,16,6]))
1--2--
#consecutive(alternate output)
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    res1=str(res)
    token='abc2d'
    result=''
    i,j=0,0
    while i<len(res1) and j<len(token):
        result+=res1[i]+token[j]
        i+=1
        j+=1
    result+=res1[i:]+token[j:]
    return result
print(consecutive([2,16,6]))
1a2bc2d
#consecutive(add '-' after every character)
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    res1=str(res)
    fin =""
    count=0
    for i in res1:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(consecutive([2,16,6]))
1-2
#consecutive(if char in token, replace with '-')
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    res1=str(res)
    result=[]
    token='abcd2'
    for char in res1:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(consecutive([2,16,6]))
1_
#consecutive(if char in token,remove those characters,if all the characters are removed then return empty)
def consecutive(arr):
    arr.sort()
    mins=min(arr)
    maxs=max(arr)
    length=[]
    for i in range(mins,maxs):
        if i not in arr:
            length.append(i)
    res=len(length)
    res1=str(res)
    result=''
    token='abc1d2'
    for char in res1:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
consecutive([2,16,6])