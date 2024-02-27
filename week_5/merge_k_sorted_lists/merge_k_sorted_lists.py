import heap as h

def merge_k_sorted_lists(lists):
    sorted_list = []
    pointers = []
    heap = h.Heap()

    for index, list in enumerate(lists):
        # We always insert into a heap an array that contains a value, and an integer telling us
        # which of the k sorted lists the value came from.
        # This integer is the index of the 'lists' array that was inputted into this method.
        heap.insert([list[0], index])
        pointers.append(1)

    while heap.not_empty():
        popped_item = heap.pop()
        popped_value = popped_item[0]
        sorted_list.append(popped_value)

        # The current_list represents which list the popped value came from:
        current_list = popped_item[1]
        if pointers[current_list] < len(lists[current_list]):
            next_item_from_current_list = lists[current_list][pointers[current_list]]
            heap.insert([next_item_from_current_list, current_list])
            pointers[current_list] += 1
    
    return sorted_list
