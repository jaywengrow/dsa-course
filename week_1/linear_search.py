# Example of O(N) algorithm - LINEAR TIME

def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index

    return None


array = [6, 3, 1, 0, 4, 2, 9, 7]
print(linear_search(array, 4))
