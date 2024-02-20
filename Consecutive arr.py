#Find number of consecutive arrays
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
print(s)
6 7 3 1 100 102 6 12
2
#find number consecutive arrays(reverse both and append semi colon)
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
token='abcd'
token1=token[::-1]
print(f'{s}:{token1}')
6 7 3 1 100 102 6 12
2:dcba
#find number consecutive arrays(replace 4th character with '-')
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
token='abcd'
res=str(s)+token
res_list=list(res)
for i in range(3,len(res),4):
    res_list[i]='-'
res=''.join(res_list)
print(res)
6 7 3 1 100 102 6 12
2ab-d
#find number consecutive arrays(replace 3rd character with 'x')
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
token='abcd'
res=str(s)+token
res_list=list(res)
for i in range(2,len(res),3):
    res_list[i]='x'
res=''.join(res_list)
print(res)
6 7 3 1 100 102 6 12
2axcd
#find number consecutive arrays(add '--' before and after char,if char in token)
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
s1=str(s)
token='ab2cd'
res=''
for char in s1:
    if char in token:
        res+=f'--{char}--'
    else:
        res+=char
print(res)
6 7 3 1 100 102 6 12
--2--
#find number consecutive arrays(alternate output)
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
s1=str(s)
token='ab2cd'
res=''
i,j=0,0
while i<len(s1) and j<len(token):
    res+=s1[i]+token[j]
    i+=1
    j+=1
res+=s1[i:]+token[j:]
print(res)
6 7 3 1 100 102 6 12
2ab2cd
#find number consecutive arrays(add '-' after every character)
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
s1=str(s)
token='ab2cd'
res=s1+token
fin =""
count=0
for i in res:
    fin+=i
    count+=1
    if count==1:
        fin+="-"
        count=0
print(fin[:-1])
6 7 3 1 100 102 6 12
2-a-b-2-c-d
#find number consecutive arrays(if char in token, replace with '-')
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
s1=str(s)
token='abcd'
res=[]
for char in s1:
    if char in token:
        res.append('_')
    else:
        res.append(char)
print(''.join(res))
6 7 3 1 100 102 6 12
2
#find number consecutive arrays(if char in token,remove those characters,if all the characters are removed then return empty)
n=list(map(int,input().split()))
n.sort()
g=[]
cg=[n[0]]
for i in range(1,len(n)):
    if n[i]==n[i-1]+1:
        cg.append(n[i])
    else:
        g.append(cg)
        cg=[n[i]]
g.append(cg)
x=max(g,key=len)
s=len(x)
s1=str(s)
token='ab2cd'
res=''
for char in s1:
    if char.lower() not in token.lower():
        res+=char
if res:
    print(res)
else:
    print('EMPTY')