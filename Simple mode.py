#simple mode
def simple_mode(arr):
    counts={}
    for num in arr:
        counts[num]=counts.get(num,0)+1
    max_count=max(counts.values())
    modes=[num for num,count in counts.items() if count==max_count]
    if max_count==1 or len(modes)==len(arr):
        return -1
    else:
        return modes[0]
print(simple_mode([10,4,5,4,2]))
4
#simple mode(reverse both and append semi colon)
import statistics
def me(arr):
    a=statistics.mode(arr)
    res=str(a)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res}:{token1}'
print(me([10,41,5,41,2]))
14:dcba
#simple mode(replace 4th character with '-')
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='abcd'
    res=str(a)+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(me([10,41,5,41,2]))
41a-cd
#simple mode(replace 3rd character with 'x')
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='abcd'
    res=str(a)+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(me([10,41,5,41,2]))
41xbcx
#simple mode(add '--' before and after char,if char in token)
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='abc1d'
    res=''
    for char in str(a):
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(me([10,41,5,41,2]))
4--1--
#simple mode(alternate output)
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='abc'
    res=''
    a1=str(a)
    i,j=0,0
    while i<len(a1) and j<len(token):
        res+=a1[i]+token[j]
        i+=1
        j+=1
    res+=a1[i:]+token[j:]
    return res
print(me([5,41,10,41,2]))
4a1bc
#simple mode(add '-' after every character)
import statistics
def me(arr):
    a=statistics.mode(arr)
    fin =""
    count=0
    for i in str(a):
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(me([10,41,5,41,2]))
4-1
#simple mode(if char in token, replace with '-')
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='ab1cd'
    res=[]
    for char in str(a):
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(me([10,41,5,41,2]))
4_
#simple mode(if char in token,remove those characters,if all the characters are removed then return empty)
import statistics
def me(arr):
    a=statistics.mode(arr)
    token='ab1c4d'
    res=''
    for char in str(a):
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
me([5,41,10,41,2])