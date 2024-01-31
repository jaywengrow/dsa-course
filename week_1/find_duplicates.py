# Example of O(N^2) algorithm - QUADRATIC TIME

def has_duplicate_value(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (i != j) and (array[i] == array[j]):
                return True

    return False


array = [4, 7, 1, 0, 2, 8, 5]
has_duplicate_value(array)
