# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character(if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final input_string is negative or positive respectively. Assume the input_string is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input_string is reached. The rest of the string is ignored.
# Convert these digits into an integer(i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary(from step 2).
# If the integer is out of the 32-bit signed integer range[-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than - 231 should be clamped to - 231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final input_string.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


# Example 1:

# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in , the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# ^
# Step 3: "42" ("42" is read in )
# ^
# The parsed integer is 42.
# Since 42 is in the range[-231, 231 - 1], the final input_string is 42.
# Example 2:

# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
# ^
# Step 2: "   -42" ('-' is read, so the input_string should be negative)
# ^
# Step 3: "   -42" ("42" is read in )
# ^
# The parsed integer is -42.
# Since - 42 is in the range[-231, 231 - 1], the final input_string is -42.
# Example 3:

# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
# ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
# ^
# Step 3: "4193 with words" ("4193" is read in
#                            reading stops because the next character is a non-digit)
# ^
# The parsed integer is 4193.
# Since 4193 is in the range[-231, 231 - 1], the final input_string is 4193.


# Constraints:

# 0 <= s.length <= 200
# s consists of English letters(lower-case and upper-case), digits(0-9), ' ', '+', '-', and '.'.


def solution(s):
    input_string = s.lstrip(" ")
    sign = 1
    output_integer = 0

    if len(input_string) == 0:
        return output_integer
    elif input_string[0] == "-":
        sign = -1
        input_string = input_string[1:]
    elif input_string[0] == "+":
        input_string = input_string[1:]

    min_value = -2**31
    max_value = 2**31 - 1

    for char in input_string:

        if 48 <= ord(char) <= 57:
            output_integer = output_integer * 10 + int(char)
            if sign > 0 and output_integer >= max_value:
                return max_value
            elif sign < 0 and -1*output_integer <= min_value:
                return min_value
        else:
            break

    return output_integer*sign
