# Last Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# The problem here is that the result of LIS for subarrays doesn't return
# enough info to make a decision. For we need to know not only the LIS
# of the subarray, but also the LIS of EVERY subarray to know if the
# current value (array[0]) can be joined to each LIS.
# For example, [6, 7, 8, 9, 1, 2, 3] - Both 7, 8, 9 and 1, 2, 3 form LIS's
# of length 3. However, the 6 can only be joined to 7, 8, 9.
# A solution for this is that LIS is not recursive itself, but calls a
# rescursive method that DOES return enough info. In this case, the recursive
# method (lis_if_include_last_value) which returns the LIS assuming that
# array[0] IS PART OF THE SEQUENCE. So, [12, 3, 4, 5] will return 1, since
# if 12 is part of the sequence, then the LIS is 1. This recursive method
# DOES return enough info to simply call itself on subarrays.
# Once we have this info,the lis method iterates through the
# lis_if_include_last_value of each value in the array and chooses the
# longest one. This is logical, since if I know the LIS that ends at each
# value (if that value is included), these are all the COMPLETE
# increasing sequences to choose from. The longest such one will be the LIS


def lis_if_include_last_value(array):
    if len(array) == 1:
        return 1

    best_lis = float('-inf')

    for i in range(1, len(array)):
        lis_for_i = lis_if_include_last_value(array[i:])

        if array[0] < array[i]:
            current_lis = lis_for_i + 1
        else:
            current_lis = 1

        if current_lis > best_lis:
            best_lis = current_lis

    return best_lis


def lis(array):
    best_lis = float('-inf')

    for i in range(len(array)):
        lis_for_i = lis_if_include_last_value(array[i:])
        if lis_for_i > best_lis:
            best_lis = lis_for_i

    return best_lis


print(lis_if_include_last_value([11, 12, 2, 3, 4]))                # length: 2
print(lis_if_include_last_value([10, 11, 12, 1, 2, 3, 4]))         # length: 3
print(lis_if_include_last_value([0, 1, 0, 3, 2, 3]))               # length: 4
print(lis_if_include_last_value([10, 9, 2, 5, 3, 7, 101, 18]))     # length: 2
print(lis_if_include_last_value([7, 7, 7, 7, 7, 7]))               # length: 1
print(lis_if_include_last_value([5, 3, 4]))                        # length: 1
print
print
print(lis([11, 12, 2, 3, 4]))                # length: 3
print(lis([10, 11, 12, 1, 2, 3, 4]))         # length: 4
print(lis([0, 1, 0, 3, 2, 3]))               # length: 4
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))     # length: 4
print(lis([7, 7, 7, 7, 7, 7]))               # length: 1
print(lis([5, 3, 4]))                        # length: 2
