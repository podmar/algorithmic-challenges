# Given n non-negative integers representing an elevation map where the width of each bar is 1. Compute how much water it can trap after raining!

def solution(array: list[int]) -> int:

    # define the max on the left for each element in the list

    rain_volume = 0

    if len(array) < 3:
        return rain_volume

    for index in range(1, len(array) - 1):  # i=1, max_l=4,
        max_left = array[0]
        for left_index in range(index):
            max_left = max(array[left_index], max_left)

        max_right = array[-1]  # m_r = 0, mr=3
        for right_index in range(index + 1, len(array) - 1):
            max_right = max(array[right_index], max_right)

        trapped_rain = min(max_left, max_right) - array[index]
        if trapped_rain > 0:
            rain_volume += trapped_rain
    return rain_volume
