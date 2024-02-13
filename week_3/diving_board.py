def diving_board(k, hash_table):
    shorter = 1
    longer = 10

    if k == 1:
        return [shorter, longer]

    old_lengths = diving_board(k - 1, hash_table)
    new_lengths = []
    for length in old_lengths:
        if not hash_table.get(length + shorter):
            hash_table[length + shorter] = True
            new_lengths.append(length + shorter)
        if not hash_table.get(length + longer):
            hash_table[length + longer] = True
            new_lengths.append(length + longer)

    return new_lengths


print(diving_board(1, {}))
print(diving_board(2, {}))
print(diving_board(3, {}))
print(diving_board(4, {}))
