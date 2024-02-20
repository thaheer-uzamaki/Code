#triple double
def triple_double(num1,num2):
    num1_str=str(num1)
    num2_str=str(num2)
    for i in range(10):
        triple_str=str(i)*3
        double_str=str(i)*2
        if triple_str in num1_str and double_str in num2_str:
            return 1
    return 0
num1=int(input())
num2=int(input())
print(triple_double(num1,num2))
456667
456778
0
#say look
def say_look(string):
    result=''
    n=len(string)
    i=0
    while i<n:
        count=1
        while(i<(n-1) and string[i]==string[i+1]):
            count+=1
            i+=1
        result+=str(count)+string[i]
        i+=1
    return result
print(say_look(input()))