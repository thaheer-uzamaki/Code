#distinct list
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    return set2
print(distinct_list([1,2,2,2,2,3]))
3
#distinct_list(reverse both and append semi colon)
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    a1=a[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{a1}:{token1}'
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
01:dcba
#distinct_list(replace 4th character with '-')
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='abcd'
    res=a+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
10a-cd
#distinct_list(replace 3rd character with 'x')
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='abcd'
    res=a+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
10xbcx
#distinct_list(add '--' before and after char,if char in token)
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='abc0d'
    res=''
    for char in a:
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
1--0--
#distinct_list(alternate output)
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='abcd'
    res=''
    i,j=0,0
    while i<len(a) and j<len(token):
        res+=a[i]+token[j]
        i+=1
        j+=1
    res+=a[i:]+token[j:]
    return res
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
1a0bcd
#distinct_list(add '-' after every character)
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    fin =""
    count=0
    for i in a:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
1-0
#distinct_list(if char in token, replace with '-')
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='ab0cd'
    res=[]
    for char in a:
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3]))
1_
#distinct_list(if char in token,remove those characters,if all the characters are removed then return empty)
def distinct_list(arr):
    set1=list(set(arr))
    set2=len(arr)-len(set1)
    a=str(set2)
    token='ab10cd'
    res=''
    for char in a:
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
distinct_list([1,2,2,2,2,2,2,2,2,2,2,2,3])