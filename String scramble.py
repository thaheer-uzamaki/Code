#string scramble
def string_scramble(str1,str2):
    outer=str1
    inner=str2
    for char in inner:
        if char not in outer:
            return False
        new=outer.replace(char,'')
        outer=new
    return True
str1=input()
str2=input()
print(string_scramble(str1,str2))