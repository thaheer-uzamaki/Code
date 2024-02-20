def EvenPairs(s):
    for i in range(len(s) -1):
        if s[i].isdigit() and s[i+1].isdigit():
            for j in range(i+1, len(s)):
                if not s[j].isdigit():
                    break
                if int(s[j]) % 2 == 0 and int(s[i]) % 2 == 0:
                    return True
    return False
print(EvenPairs(input()))
f09r27i8e67
False
#camel case
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    return new
print(camelcase(input()))
cats AND*Dogs-are Awesome
catsAndDogsAreAwesome
#camel case(reverse both and append semi colon)
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    res=new[::-1]
    #print(res)
    token='abcd'
    token1=token[::-1]
    return f'{res}:{token1}'
print(camelcase(input()))
cats AND*Dogs-are Awesome
emosewAerAsgoDdnAstac:dcba
#camel case(replace 4th character with '-')
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='pqrstuv'
    res=new+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(camelcase(input()))
cats AND*Dogs-are Awesome
cat-And-ogs-reA-eso-epq-stu-
#camel case(replace 3rd character with 'x')
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='pqrstuv'
    res=new+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(camelcase(input()))
cats AND*Dogs-are Awesome
caxsAxdDxgsxrexwexomxpqxstxv
#camel case(add '--' before and after char,if char in token)
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='pqrst'
    res=''
    for char in new:
        if char in token:
            res+=f'--{char}--'
        else:
            res+=char
    return res
print(camelcase(input()))
cats AND*Dogs-are Awesome
ca--t----s--AndDog--s--A--r--eAwe--s--ome
#camelcase(alternate output)
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='pqrst'
    res=''
    i,j=0,0
    while i<len(new) and j<len(token):
        res+=new[i]+token[j]
        i+=1
        j+=1
    res+=new[i:]+token[j:]
    return res
print(camelcase(input()))
cats AND*Dogs-are Awesome
cpaqtrssAtndDogsAreAwesome
#camelcase(add '-' after every character)
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    fin =""
    count=0
    for i in new:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(camelcase(input()))
cats AND*Dogs-are Awesome
c-a-t-s-A-n-d-D-o-g-s-A-r-e-A-w-e-s-o-m-e
#camelcase(if char in token, replace with '-')
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='abd'
    res=[]
    for char in new:
        if char in token:
            res.append('_')
        else:
            res.append(char)
    return ''.join(res)
print(camelcase(input()))
    
cats AND*Dogs-are Awesome
c_tsAn_DogsAreAwesome
#camelcase(if char in token,remove those characters,if all the characters are removed then return empty)
def camelcase(string):
    words = string.title()
    new = ''
    camel = words[0].lower()+words[1:]
    for i in  camel:
        if i.isalpha():
            new += i
    token='abd'
    res=''
    for char in new:
        if char.lower() not  in token.lower():
            res+=char
    if res:
        print(res)
    else:
        print('EMPTY')
camelcase(input())
