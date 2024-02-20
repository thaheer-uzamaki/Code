#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>#mutiple of 3 and 5 and sum of them
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    return result
print(multiple(int(input())))
10
23
#multiple of 3 and 5 and sum of them(reverse both and append semi colon)
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    result1=str(result)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{result1}:{token1}'
print(multiple(int(input())))
10
32:dcba
#multiple of 3 and 5 and sum of them(replace 4th character with '-')
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abcd'
    res1=str(result)+token
    res_list=list(res1)
    for i in range(3,len(res1),4):
        res_list[i]='-'
    res1=''.join(res_list)
    return res1
print(multiple(int(input())))
10
23a-cd
#multiple of 3 and 5 and sum of them(replace 43rd character with 'x')
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abcd'
    res1=str(result)+token
    res_list=list(res1)
    for i in range(2,len(res1),3):
        res_list[i]='x'
    res1=''.join(res_list)
    return res1
print(multiple(int(input())))
10
23xbcx
#multiple of 3 and 5 and sum of them(add '--' before and after char,if char in token)
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abc3d'
    res1=''
    for char in str(result):
        if char in token:
            res1+=f'--{char}--'
        else:
            res1+=char
    return res1
print(multiple(int(input())))
10
2--3--
#multiple of 3 and 5 and sum of them(alternate output)
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    result1=str(result)
    token='abc3d'
    res1=''
    i,j=0,0
    while i<len(result1) and j<len(token):
        res1+=result1[i]+token[j]
        i+=1
        j+=1
    res1+=result1[i:]+token[j:]
    return res1
print(multiple(int(input())))
10
2a3bc3d
#multiple of 3 and 5 and sum of them(add '-' after every character)
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abc3d'
    result1=str(result)+token
    fin =""
    count=0
    for i in result1:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(multiple(int(input())))
10
2-3-a-b-c-3-d
#multiple of 3 and 5 and sum of them(if char in token, replace with '-')
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abc3d'
    res1=[]
    for char in str(result):
        if char in token:
            res1.append('_')
        else:
            res1.append(char)
    return ''.join(res1)
print(multiple(int(input())))
10
2_
#multiple of 3 and 5 and sum of them(if char in token,remove those characters,if all the characters are removed then return empty)
def multiple(num):
    res=[]
    for num in range(1,num):
        if num%3==0:
            res.append(num)
        elif num%5==0:
            res.append(num)
    result=sum(res)
    token='abc3d'
    res1=''
    for char in str(result):
        if char.lower() not in token.lower():
            res1+=char
    if res1:
        print(res1)
    else:
        print('EMPTY')
multiple(int(input()))[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
my_array=[9,7,10,5,3,8,12,1]
bubble_sort(my_array)
print(my_array)