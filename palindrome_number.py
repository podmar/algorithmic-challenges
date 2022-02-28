# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

###

test_1 = 121
test_2 = -121
test_3 = 123
test_4 = -2

def string_solution(x): 
    is_palindrome = False

    s = str(x)
    s_backwards = s[::-1]

    if s == s_backwards: 
        is_palindrome = True

    return is_palindrome


#print(string_solution(test_1), string_solution(test_2), string_solution(test_3), string_solution(test_4))

#Runtime: 76 ms, faster than 55.30% of Python online submissions for Palindrome Number.
#Memory Usage: 13.5 MB, less than 40.03% of Python online submissions for Palindrome Number.

# [x] How to solve without turning into string? 
# USING MATH MODULE and Log10

import math

def log10_solution(x): 
    is_palindrome = False
    no_digits = 0

    if x > 0: 
        no_digits = int(math.log10(x)+1)
    elif x == 0:
        no_digits = 1
    else: 
        no_digits = int(math.log10(-x)+2)

    remaining_number = x
    digit_list = []

    for i in range(no_digits-1,-1,-1): 
        digit = remaining_number//(10**(i))
        digit_list.append(digit)
        remaining_number = remaining_number - digit*(10**(i))

    backwards_digit_list = digit_list[::-1]

    if digit_list == backwards_digit_list: 
        is_palindrome = True

    return is_palindrome

print(log10_solution(test_1), log10_solution(test_2), log10_solution(test_3), log10_solution(test_4))

# Runtime: 82 ms, faster than 49.00% of Python online submissions for Palindrome Number.
# Memory Usage: 13.4 MB, less than 66.69% of Python online submissions for Palindrome Number.

#USING MODULO OPERATOR

def modulo_solution(x): 
    is_palindrome = False

    def reversed(num): 
        reversed = 0
        while num > 0:
            reversed = (reversed * 10) + (num % 10)
            num = num // 10
        return reversed

    if reversed(x) == x: 
        is_palindrome = True

    return is_palindrome

print(modulo_solution(test_1), modulo_solution(test_2), modulo_solution(test_3), modulo_solution(test_4))

# Runtime: 99 ms, faster than 34.25% of Python online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 87.96% of Python online submissions for Palindrome Number.