# sort a T[] one-dimensional array of integers in O(N) / linear running time - and without any extra memory.
# The array can contain values: 0, 1 and 2

# 1 is the pivot value
# a marks start of ones, b marks start of twos, c marks the current index

def solution(array):
    a = 0
    b = len(array) - 1
    c = 0

    while c <= b:
        if array[c] < 1:
            array[a], array[c] = array[c], array[a]
            a += 1
            c += 1
        elif array[c] > 1:
            array[c], array[b] = array[b], array[c]
            b -= 1
        else:
            c += 1

    return array
