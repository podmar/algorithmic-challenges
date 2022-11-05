# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

def solution_draft(s):

    def is_digit(char):
        if 47 <= ord(char) <= 58:
            return True

    def are_digits(chars):
        result = True
        for char in chars:
            if ord(char) < 47 or ord(char) > 58:
                result = False
                break
        return result

    # allowed are: ".", digits 0-9, "e"
    def has_allowed_signs(chars):
        allowed_signs_unicode = [*range(46, 59), 101]
        for char in chars:
            if ord(char) in allowed_signs_unicode:
                continue
            else:
                return False

        return True

    def is_integer(input):

        # has a plus or minus sign at the beginning
        if input[0] == "+" or input[0] == "-":
            input = input[1:]

        # consists only of digits
        if are_digits(input):
            return True

        # starts with a dot and digits after
        if input[0] == "." and are_digits(input[1:]):
            return True

        # starts with digits and a dot after
        if input[-1] == "." and are_digits(input[:-1]):
            return True

        # starts with digits, dot and digits after

        input.lower()

        for i, char in enumerate(input):
            if is_digit(char):
                continue
            elif char == ".":
                continue
            else:
                return False

        return True

        # for i, char in enumerate(input):
        #     if is_digit(char):
        #         continue
        #     elif is_digit(input[i-1]) and char == ".":
        #         continue
        #     else:
        #         result = False

        return result

    # is_decimal_number
    # is_e_with_integer

    is_valid_number = is_integer(s)

    return is_valid_number

# loop through all elements of a string and create a dictionary with keys: digit, e, dot, not_allowed; remove plus/minus
# save the index of every occurence in a list in the dictionary
# if len(not_allowed) != 0, return false
# if len . / e > 1, return false
# positioning of the dot vs e conditions
