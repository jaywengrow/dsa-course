import heap
import merge_k_sorted_lists


def assert_equal(x, y):
    if x == y:
        print(".")
    else:
        print("FAIL")

# Test min-heap
h = heap.Heap()
h.insert(5)
h.insert(3)
h.insert(9)
h.insert(0)
h.insert(6)
a = []
a.append(h.pop())
a.append(h.pop())
a.append(h.pop())
a.append(h.pop())
a.append(h.pop())
assert_equal(a, [0, 3, 5, 6, 9])


# Merge K Sorted Lists
lists = [[0, 3, 6, 9, 14], [4, 5, 20, 33], [1, 2, 10, 50, 54, 89], [8, 15, 21, 25]]
sorted_list = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 14, 15, 20, 21, 25, 33, 50, 54, 89]
assert_equal(merge_k_sorted_lists.merge_k_sorted_lists(lists), sorted_list)
