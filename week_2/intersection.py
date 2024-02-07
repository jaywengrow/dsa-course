def intersection(array_1, array_2):
    hash_table = {}

    for value in array_1:
        hash_table[value] = True

    result_array = []

    for value in array_2:
        if hash_table.get(value):
            result_array.append(value)

    return result_array


print(intersection([1, 3, 5, 7, 9], [9, 2, 3, 6, 8, 1]))
