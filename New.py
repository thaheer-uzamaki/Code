#Decimal Point
def StringChallenge(strArr):
    input_str = strArr[0]
    if input_str.count(".") != 1 or input_str.count(",") > 2:
        return "false"
    parts = input_str.split(".")
    if len(parts) != 2:
        return "false"
    integer_part, fractional_part = parts
    if not integer_part.isdigit() or len(integer_part) > 3:
        return "false"
    if not all(c.isdigit() for c in fractional_part):
        return "false"
    return "true"
print(StringChallenge(["0.232567"])) 
true
#wave sort
def WaveSorting(arr):
    arr.sort()
    array1 = arr[:len(arr)//2]
    array2 = arr[len(arr)//2:]
    for i in range(len(array1)):
        if array1[i] >= array2[i]:
            return False
    return True

# Test the function
print(WaveSorting(list(map(int, input().split()))))
0 1 2 4 1 1 1
False
# third greatest
def ThirdGreatest(strArr):
    wordLengthArray = [len(word) for word in strArr]
    wordLengthArray.sort()
    thirdGreatest = wordLengthArray[-3]
    index = 0
    for i, word in enumerate(strArr):
        if len(word) == thirdGreatest:
            index = i
    return strArr[index]

# Test the function
print(ThirdGreatest(input().split()))
abc defg z hijk
abc
#super increasing
def superinc(arr):
    sums = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > sums:
            sums+= arr[i]
        else:
            return False
    return True
superinc([1,2,5,10])
True
#sum multiplier
from itertools import combinations
def summul(arr):
    sums = sum(arr)*2
    for combo in combinations(arr,2):
        if combo[0]*combo[1]  > sums:
            return True
    return False
summul([1, 1, 2, 10, 3, 1, 12])
True
def elementmerger(arr):
    new = []
    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        new.append(diff)
        
    if len(new) == 1:
        for i in new:
            return i
    else:
        return elementmerger(new)
elementmerger([5, 7, 16, 1, 2])
7
#ascii conversion
def asci(ip):
    new = ''
    for i in ip:
        if i == ' ':
            new += ' '
        else:
            new += str(ord(i))
    return new
asci('abc   **')
'979899   4242'
#binary reversal
def binaryreverse(ip):
    binary = bin(int(ip))[2:]
    pad_binary = binary.rjust((len(binary)+7)//8*8,'0')
    rev_bin = pad_binary[::-1]
    decimal_r = int(rev_bin,2)
    return decimal_r
binaryreverse('213')
171
#swap digits
def swap_digits(word):
    digit_positions = [i for i, char in enumerate(word) if char.isdigit()]
    #print(digit_positions)
    if len(digit_positions) == 2:
        new_word = list(word)
        new_word[digit_positions[0]], new_word[digit_positions[1]] = new_word[digit_positions[1]], new_word[digit_positions[0]]
        return ''.join(new_word)
 
    return word
 
def swapp(ip):
    words = ip.split()
    new_words = []
 
    for word in words:
        swapped_word = word.swapcase()
        swapped_word = swap_digits(swapped_word)
        new_words.append(swapped_word)
 
    return ' '.join(new_words)
print(swapp(input()))
Hel2l3o -5LOL6
hEL3L2O -6lol5
#matching character
def matching_character(string):
    letter_counts = {}
    for letter in string:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    pair_count = 0
    for count in letter_counts.values():
        pair_count += count // 2  
    return pair_count
print(matching_character(input()))
mamamamamama
6
def MissingDigitII(s):
    # Split the equation into two sides
    equation_sides = s.split('=')
    left_side = equation_sides[0].strip()
    right_side = equation_sides[1].strip()
 
    # Iterate through digits from 0 to 9 for the first missing digit
    for i in range(10):
        equation1 = left_side.replace('?', str(i))
 
        # Iterate through digits from 0 to 9 for the second missing digit
        for j in range(10):
            equation2 = right_side.replace('?', str(j))
 
            # Evaluate both sides of the equation
            if eval(equation1) == eval(equation2):
                return f"{i} {j}"
 
# Test cases
print(MissingDigitII("56? * 106 = 5?678"))  # Output: "3 9"
3 9
# square
def m(num):
    if num ==1:
        return 0
    i=1
    while True:
        s=i*i
        if len(str(s))==num:
            return i
        i+=1
num=6
m(num)