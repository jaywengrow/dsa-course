# Version #1: Makes a brand new array -> O(N) space
def make_uppercase(array):
    new_array = []

    for string in array:
        new_array.append(string.upper())

    return new_array

# Version #2: Modifies the original array - i.e. IN PLACE -> O(1) Space
def make_uppercase(array):
    for index in range(len(array)):
        array[index] = array[index].upper()

    return array

# Input -> ["a", "b", "c"]
# Ouput -> ["A", "B", "C"]