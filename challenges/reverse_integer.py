# #Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers(signed or unsigned).


# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21


# Constraints:

# -231 <= x <= 231 - 1

# reverse integer

def solution(n):

    def reverse(num):
        reversed_number = 0

        while num > 0:
            reversed_number *= 10
            reversed_number += num % 10
            num = num // 10

        return reversed_number

    result = 0

    if n >= -2**31 and n < 0:
        result = reverse(abs(n)) * -1
    elif (n < (2**32)-1) and n > 0:
        result = reverse(n)

    return result


print(solution(2))
