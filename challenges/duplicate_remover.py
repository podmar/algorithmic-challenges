# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# Example 2:

# Input: s = "azxxzy"
# Output: "ay"
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

#############

def solution_1(s): 
    starting_len = len(s)
    new_len = 0

    while starting_len != new_len: 
        starting_len = len(s)

        try: 
            for i in range(0, len(s)): 

                if s[i] == s[i + 1]: 
                    s = s[:i] + s[i+2:]
                    new_len = len(s)
                    break

        except IndexError: 
            pass

    return s

# managed to except the erron on solution_1, but the funtion is very slopw: time limit exceded

def solution_2(s): 

     arr = []
     index = 0

     for i in s: 
         if len(arr) == 0 or i != arr[index]: 
             arr.append(i)
         elif i == arr[index]: 
             arr.pop(index)

         index = len(arr)-1

     final_s = ""

     for l in arr:
         final_s += l
    
     return final_s

# Runtime: 1418 ms, faster than 6.94% of Python online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.6 MB, less than 63.73% of Python online submissions for Remove All Adjacent Duplicates In String.
