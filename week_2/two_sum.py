def two_sum(array):
    hash_table = {}

    for value in array:
        if hash_table.get(10 - value):
            return True
        else:
            hash_table[value] = True

    return False
