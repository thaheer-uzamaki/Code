#vowel count
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    return count
print(vowel_count(input()))

#vowel count(reverse both and append semi colon)
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    res=str(count)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res}:{token1}'
print(vowel_count(input()))

#vowel count(replace 4th character with '-')
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abcdef'
    res=str(count)+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(vowel_count(input()))

#vowel count(replace 3rd character with 'x')
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abcdef'
    res=str(count)+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(vowel_count(input()))

#vowel count(add '--' before and after char,if char in token)
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abc5de'
    res=''
    for char in str(count):
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(vowel_count(input()))

#vowel_count(alternate output)
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abcde'
    res1=str(count)
    res=''
    i,j=0,0
    while i<len(res1) and j<len(token):
        res+=res1[i]+token[j]
        i+=1
        j+=1
    res+=res1[i:]+token[j:]
    return res
print(vowel_count(input()))

#vowel_count(add '-' after every character)
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    fin =""
    count1=0
    for i in str(count):
        fin+=i
        count1+=1
        if count1==1:
            fin+="-"
            count1=0
    return fin[:-1]
print(vowel_count(input()))

#vowel_count(if char in token, replace with '-')
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abc5de'
    res=[]
    for char in str(count):
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(vowel_count(input()))

#vowel count(if char in token,remove those characters,if all the characters are removed then return empty)
def vowel_count(string):
    vowel='aeiou'
    count=0
    for char in string.lower():
        if char in vowel:
            count+=1
    token='abcde'
    res=''
    for char in str(count):
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
vowel_count(input())