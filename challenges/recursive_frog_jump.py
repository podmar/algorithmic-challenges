# There are 10 stones in a line leading across the river, separated by 1 foot, and the frog is
# only ever able to jump one foot forward to the next stone, or two feet forward to the stone
# after the next. In how many different ways can he jump exactly 11 feet to the other side of
# the river?

def solution(n: int) -> int:

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        result = solution(n-1) + solution(n-2)

    return result


if __name__ == "__main__":
    test = solution(6)
    print(test)
