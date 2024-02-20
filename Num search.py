#number search
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    return round(float(num_total)/letter_count)
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2
#number search(reverse both and append semi colon)
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    res1=str(res)[::-1]
    token='abcd'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2:dcba
#number search(replace 4th character with '-')
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(3,len(result),4):
        res_list[i]='-'
    result=''.join(res_list)
    return result
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2ab-d
#number search(replace 3rd character with 'x')
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    token='abcd'
    result=str(res)+token
    res_list=list(result)
    for i in range(2,len(result),3):
        res_list[i]='x'
    result=''.join(res_list)
    return result
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2axcd
#number search(add '--' before and after char,if char in token)
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    token='ab2cd'
    result=''
    for char in str(res):
        if char in token:
            result+=f'--{char}--'
        else:
            result+=char
    return result
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
--2--
#number search(alternate output)
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    res1=str(res)
    token='ab2cd'
    result=''
    i,j=0,0
    while i<len(res1) and j<len(token):
        result+=res1[i]+token[j]
        i+=1
        j+=1
    result+=res1[i:]+token[j:]
    return result
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2ab2cd
#number search(add '-' after every character)
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    res1=str(res)
    token='abcd'
    result=res1+token
    fin =""
    count=0
    for i in result:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
2-a-b-c-d
#number search(if char in token, replace with '-')
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    res1=str(res)
    token='ab2cd'
    result=[]
    for char in res1:
        if char in token:
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)
print(number_search(input()))
Hello6 9World 2, Nic8e D7ay!
_
#number search(if char in token,remove those characters,if all the characters are removed then return empty)
def number_search(string):
    letter_count=0
    num_total=0
    for char in string:
        if char.isalpha():
            letter_count+=1
        elif char.isdigit():
            num_total+=int(char)
    res=round(float(num_total)/letter_count)
    res1=str(res)
    token='abcd'
    result=''
    for char in res1:
        if char.lower() not in token.lower():
            result+=char
    if result:
        print(result)
    else:
        print('EMPTY')
number_search(input())