#password check
def simple_password(string):
    if not any (char.isupper() for char in string):
        return False
    elif not any (char.isdigit() for char in string):
        return False
    elif not any(char in "!@#$%^&*()-_+={}[]:;\"'<>,.?/~" for char in string):
        return False
    elif 'password' in string.lower():
        return False
    elif not 7 < len(string) < 31:
        return False
    return True
print(simple_password(input()))