#second great low
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    return small,great
print(sec_great_low([7,7,12,96,106]))
    
(12, 96)
#second great low(reverse both and append semi colon)
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=small,great
    res1=res[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(sec_great_low([7,7,12,96,106]))
(96, 12):dcba
#second great low(replace 4th character with '-')
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=small,great
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(sec_great_low([7,7,12,96,106]))
(12- 96-abc-
#sec_great_low(replace 3rd character with 'x')
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=small,great
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(sec_great_low([7,7,12,96,106]))
(1x, x6)xbcx
#sec_great_low(add '--' before and after char,if char in token)
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=small,great
    token='abcd1'
    result=''
    for char in str(res):
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(sec_great_low([7,7,12,96,106]))
(--1--2, 96)
#sec_great_low(alternate output)
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=(small,great)
    res1=str(res)
    token='abcdefghi'
    result=''
    i,j=0,0
    while i<len(res1) and j<len(token):
        result+=res1[i]+token[j]
        i+=1
        j+=1
    result+=res1[i:]+token[j:]
    return result
print(sec_great_low([7,7,12,96,106]))
(a1b2c,d e9f6g)hi
#sec_great_low(add '-' after every character)
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=(small,great)
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
print(sec_great_low([7,7,12,96,106]))
(-1-2-,- -9-6-)
#sec_great_low(if char in token, replace with '-')
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=(small,great)
    res1=str(res)
    token='abc26d'
    result=[]
    for char in res1:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(sec_great_low([7,7,12,96,106]))
(1_, 9_)
#sec_great_low(if char in token,remove those characters,if all the characters are removed then return empty)
def sec_great_low(arr):
    a=list(set(arr))
    s=sorted(a)
    great=s[-2]
    small=s[1]
    res=(small,great)
    res1=str(res)
    token='abc26d'
    result=''
    for char in res1:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else: 
        print('EMPTY')
sec_great_low([7,7,12,96,106])

