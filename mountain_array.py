# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

#https://leetcode.com/problems/valid-mountain-array/

###########

#ACTION PLAN
#find the max value, it's index and check if values right&left decrease

test = [1, 2, 7, 1, 2, 1]

def solution(arr): 

#values for testing
    ascends = 0
    descends = 0
    
    is_mountain = True

    peak = arr.index(max(arr))

    for i in range(0, peak):
        if arr[i] < arr[i+1]:
            ascends += 1
            print("The array item %i, ascends valuse is %i" %(arr[i], ascends))
        else:
            is_mountain = False
            break

    for n in range(peak, len(arr)-1): 
        if arr[n] > arr[n+1]:
            descends += 1
            print("The array item %i, descends value is %i" %(arr[n], descends))
        else:
            is_mountain = False
            break

    print("The given array is a mountain array: %r" %(is_mountain))

    return is_mountain

print(solution(test))