# https://leetcode.com/problems/house-robber/description/


def rob(array):
    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        return max(array[0], array[1])

    return max(rob(array[:-1]), rob(array[:-2]) + array[-1])


print(rob([1, 2, 3, 1]))     # 4
print(rob([2, 7, 9, 3, 1]))  # 12
