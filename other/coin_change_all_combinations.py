def coin_change(coins, amount):
    if len(coins) == 1:
        combos = []
        combo = []
        while sum(combo) + coins[0] <= amount:
            combo.append(coins[0])
            new_combo = list(combo)
            combos.append(new_combo)
        return combos

    subset_combos = coin_change(coins[1:], amount)
    combos = []
    for subset_combo in subset_combos:
        combos.append(subset_combo)
        combo = list(subset_combo)
        while sum(combo) + coins[0] <= amount:
            combo.append(coins[0])
            new_combo = list(combo)
            combos.append(new_combo)

    return combos


print(coin_change([1, 2, 5], 11))
