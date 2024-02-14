# https://leetcode.com/problems/subsets/description/


def subsets(array):
    if len(array) == 0:
        return [[]]

    smaller_subsets = subsets(array[:-1])

    total_subsets = []
    for subset in smaller_subsets:
        total_subsets.append(list(subset))
        subset.append(array[-1])
        total_subsets.append(subset)

    return total_subsets


print(subsets([1, 2, 3]))
