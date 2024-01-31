# Example of O(1) algorithm - i.e. CONSTANT TIME

def sample(array):
    if not array:
        return None

    first = array[0]
    middle = array[len(array) // 2]
    last = array[-1]

    return [first, middle, last]
