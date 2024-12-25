#https://www.geeksforgeeks.org/problems/implement-atoi/1

def myAtoi(s: str) -> int:

    # remove leading whitespaces
    s = s.lstrip()
    if len(s) == 0:
        return 0

    # check if the first character is a sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # check if the first character is a digit
    if len(s) == 0 or not s[0].isdigit():
        return 0

    # find the number
    num = 0
    for c in s:
        if not c.isdigit():
            break
        num = num * 10 + int(c)

    # apply the sign
    num *= sign

    # check if the number is within the 32-bit signed integer range
    if num < -2**31:
        return -2**31
    if num > 2**31 - 1:
        return 2**31 - 1

    return num

# Time complexity: O(n)
# Space complexity: O(1)

# Test cases
print(myAtoi("42")) #42
print(myAtoi("   -42")) #-42
print(myAtoi("4193 with words")) #4193
print(myAtoi("words and 987")) #0

# Additional test cases
print(myAtoi("3.14159")) #3
print(myAtoi("+-12")) #0
print(myAtoi("00000-42a1234")) #0
print(myAtoi("21474836460")) #2147483647
print(myAtoi("-")) #-2147483648