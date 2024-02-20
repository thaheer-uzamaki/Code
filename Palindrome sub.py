def PalindromicSubstring(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome if len(longest_palindrome) > 2 else "none"
print(PalindromicSubstring(input())) 