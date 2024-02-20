#letter count
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    return gl
print(letter_count(input()))
today is the greatest day ever
greatest
#letter count(reverse both and append semi colon)
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    gl1=gl[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{gl1}:{token1}'
print(letter_count(input()))
today is the greatest day ever
tsetaerg:dcba
#letter count(replace 4th character with '-')
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='pqrst'
    result=gl+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(letter_count(input()))
today is the greatest day ever
gre-tes-pqr-t
#letter count(replace 3rd character with 'x')
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='pqrst'
    result=gl+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(letter_count(input()))
today is the greatest day ever
grxatxstxqrxt
#letter count(add '--' before and after char,if char in token)
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='pqrst'
    result=''
    for char in gl:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(letter_count(input()))
today is the greatest day ever
g--r--ea--t--e--s----t--
#letter count(alternate output)
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='pqrst'
    result=''
    i,j=0,0
    while i<len(gl) and j<len(token):
        result+=gl[i]+token[j]
        i+=1
        j+=1
    result+=gl[i:]+token[j:]
    return result
print(letter_count(input()))
today is the greatest day ever
gprqerasttest
#letter count(add '-' after every character)
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    fin =""
    count=0
    for i in gl:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(letter_count(input()))
today is the greatest day ever
g-r-e-a-t-e-s-t
#letter count(if char in token, replace with '-')
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='abcd'
    result=[]
    for char in gl:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(letter_count(input()))
today is the greatest day
gre_test
#letter count(if char in token,remove those characters,if all the characters are removed then return empty)
def letter_count(string):
    res=string.split()
    count=0
    gl='-1'
    for i in range(len(res)):
        for j in range(len(res[i])):
            new_count=0
            for k in range(j+1,len(res[i])):
                if res[i][j]==res[i][k]:
                    new_count+=1
                    if new_count>count:
                        count=new_count
                        gl=res[i]
    token='abcd'
    result=''
    for char in gl:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
letter_count(input())
only code and comments