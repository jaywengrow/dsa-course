# https://leetcode.com/problems/coin-change/description/


def coin_change(coins, amount):
    if amount == 0:
        return 0

    min = float('inf')
    min_if_i_take_this_coin = -1

    for coin in coins:
        amount_left = amount - coin
        if amount_left >= 0:
            min_if_i_take_this_coin = coin_change(coins, amount_left) + 1
            if min_if_i_take_this_coin < min:
                min = min_if_i_take_this_coin

    if min_if_i_take_this_coin <= 0:
        min_if_i_take_this_coin = -1

    return min_if_i_take_this_coin


print(coin_change([1, 2, 5], 11))
print(coin_change([1, 2, 5], 12))
print(coin_change([2], 3))
print(coin_change([2], 1))
print(coin_change([2, 5, 10], 13))
print(coin_change([2, 5, 10], 23))
