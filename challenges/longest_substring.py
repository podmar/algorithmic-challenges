# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not .
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

# Example 1:

# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# Example 2:

# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.

# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.

def solution(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    longest_substring = 0
    current_substring = 0
    last_index = alphabet.index(s[0]) - 1

    for char in s:

        if alphabet.index(char) == last_index + 1:
            current_substring += 1
            last_index += 1
            if current_substring > longest_substring:
                longest_substring = current_substring

        else:
            last_index = alphabet.index(char)
            if current_substring > longest_substring:
                longest_substring = current_substring
            current_substring = 1

    return longest_substring
