# sort a T[] one-dimensional array of integers in O(N) running time - and without any extra memory.
# The array can contain values: 0, 1 and 2

def solution(array):
    zeroes = 0
    ones = 0
    twos = 0
    sorted_list = []

    for i in array:  # O(n)
        if i == 0:  # O(1)
            zeroes += 1
        elif i == 1:
            ones += 1
        elif i == 2:
            twos += 1

    for n in range(zeroes):
        sorted_list.append(0)
    for n in range(ones):
        sorted_list.append(1)
    for n in range(twos):
        sorted_list.append(2)

    print(sorted_list)

    return sorted_list
