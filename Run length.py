#run length
def run_length(string):
    result=''
    n=len(string)
    i=0
    while i<n:
        count=1
        while (i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    return result
print(run_length(input()))
aabbb
2a3b
#run length(reverse both and append semi colon)
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    res1=result[::-1]
    token='pqrst'
    token1=token[::-1]
    return f'{res1}:{token1}'
print(run_length(input()))
aabbb
b3a2:tsrqp
#run_length(replace 4th character with '-')
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='pqrst'
    res=result+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(run_length(input()))
aabbb
2a3-pqr-t
#run length(replace 3rd character with 'x')
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='pqrst'
    res=result+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(run_length(input()))
aabbb
2axbpxrsx
#run length(add '--' before and after char,if char in token)
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='pq3rst'
    res=''
    for char in result:
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(run_length(input()))
aabbb
2a--3--b
#runlength(alternate output)
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='pqrst'
    res=''
    i,j=0,0
    while i<len(result) and j<len(token):
        res+=result[i]+token[j]
        i+=1
        j+=1
    res+=result[i:]+token[j:]
    return res
print(run_length(input()))
aabbb
2paq3rbst
#run_length(add '-' after every character)
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    fin =""
    count=0
    for i in result:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(run_length(input()))
aabbb
2-a-3-b
#run_length(if char in token, replace with '-')
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='abcd'
    res=[]
    for char in result:
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(run_length(input()))
        
aabbb
2_3_
#run_length(if char in token,remove those characters,if all the characters are removed then return empty)
def run_length(string):
    result=''
    i=0
    n=len(string)
    while i<n:
        count=1
        while (i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    token='bcd'
    res=''
    for char in result:
        if char.lower() not in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
run_length(input())
only code and comments