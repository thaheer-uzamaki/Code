#timeconverts
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    return res
print(time_converts(int(input())))

#timeconverts(reverse both and append semi colon)
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    res1=res[::-1]
    token='abcdef'
    token1=token[::-1]
    return f'{res1}-{token1}'
print(time_converts(int(input())))

#timeconverts(replace 4th character with '-')
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='abcdefghi'
    result=res+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(time_converts(int(input())))

#timeconverts(replace 3rd character with 'x')
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='abcdefghi'
    result=res+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(time_converts(int(input())))

#timeconverts(add '--' before and after char,if char in token)
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='frgt5yh'
    result=''
    for char in res:
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(time_converts(int(input())))

#timeconverts(alternate output)
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='abcd'
    result=''
    i,j=0,0
    while i<len(res) and j<len(token):
        result+=res[i]+token[j]
        i+=1
        j+=1
    result+=res[i:]+token[j:]
    return result
print(time_converts(int(input())))

#timeconverts(add '-' after every character)
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='abcd'
    fin =""
    count=0
    for i in res:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(time_converts(int(input())))

#time_converts(if char in token, replace with '-')
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='ab5cd'
    result=[]
    for char in res:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(time_converts(int(input())))

#time_converts(if char in token,remove those characters,if all the characters are removed then return empty)
def time_converts(num):
    hrs=num//60
    mins=num%60
    res=f'{hrs}:{mins}'
    token='ab51cd:'
    result=''
    for char in res:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
time_converts(int(input()))