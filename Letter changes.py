#letter changes
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    return capi
print(letter_changes(input()))  

#letter changes(reverse both and append semi colon)
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    token='abcd'
    token1=token[::-1]
    res=capi[::-1]
    return f'{res}:{token1}'
print(letter_changes(input()))

#letter changes(replace 4th character with '-')
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    token='abcd'
    res=capi+token
    res_list=list(res)
    for i in range(3,len(res),4):
        res_list[i]='-'
    res=''.join(res_list)
    return res
print(letter_changes(input()))

#letter changes(replace 3rd character with 'x')
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    token='pqrst'
    res=capi+token
    res_list=list(res)
    for i in range(2,len(res),3):
        res_list[i]='x'
    res=''.join(res_list)
    return res
print(letter_changes(input()))

#letter changes(add '--' before and after the character, if character in token)
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    token='nhjuikb'
    ans=''
    for chars in capi:
        if chars in token:
            ans+=f'--{chars}--'
        else:
            ans+=chars
    return ans
print(letter_changes(input()))

#letter changes(alternate output)
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    token='pqrs'
    res=''
    i,j=0,0
    while i<len(capi) and j<len(token):
        res+=capi[i]+token[j]
        i+=1
        j+=1
    res+=capi[i:]+token[j:]
    return res
print(letter_changes(input()))

#letter changes(add '-' after every character)
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)
            result+=letter[index+1]
    capi=''
    for chara in result:
        if chara in 'aeiou':
            capi+=chara.upper()
        else:
            capi+=chara
    fin =""
    count=0
    for i in capi:
        fin+=i
        count+=1
        if count==1:
            fin+="-"
            count=0
    return fin[:-1]
print(letter_changes(input()))

#letter changes(if char in token, replace with '-')
def letter_changes(string):
    letter='abcdefghijklmnopqrstuvwxyz'
    result=''
    for char in string.lower():
        if char not in letter:
            result+=char
        elif char=='z':
            result+='a'
        else:
            index=letter.index(char)