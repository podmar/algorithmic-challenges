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

def solution(x): 
    is_palindrome = False

    s = str(x)
    s_backwards = s[::-1]

    if s == s_backwards: 
        is_palindrome = True

    return is_palindrome


print(solution(test_1), solution(test_2), solution(test_3))

#Runtime: 76 ms, faster than 55.30% of Python online submissions for Palindrome Number.
#Memory Usage: 13.5 MB, less than 40.03% of Python online submissions for Palindrome Number.

# How to solve without turning into string? 



