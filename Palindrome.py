#palindrome
import re
def palindrome(string):
    res=re.sub('[^a-zA-Z0-9]','',string)
    return res==res[::-1]
print(palindrome(input()))
