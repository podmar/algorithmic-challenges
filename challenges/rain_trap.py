# Given n non-negative integers representing an elevation map where the width of each bar is 1. Compute how much water it can trap after raining!

def solution(array):

    # define the max on the left for each element in the list

    rain_volume = 0

    for index in range(len(array)):
        # max_left = array[index]
        for left_index in range(index):
            max_left = max(array[left_index], array[index])
        for right_index in range(index):
            max_right = max(array[index], array[right_index])

        rain_volume = + max(max_left, max_right) - array[index]
    return rain_volume
