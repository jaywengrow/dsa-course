def lis(array, memo=None):
    if len(array) == 1:
        return {'length': 1, 'last_value': array[0]}

    best_length_so_far = 1
    best_value = array[0]

    for i in range(1, len(array)):
        sub_lis = lis(array[i:])

        if array[0] < sub_lis['last_value']:
            current_length = sub_lis['length'] + 1
            current_value = array[0]
        else:
            current_length = sub_lis['length']
            current_value = sub_lis['last_value']
        
        print(array[0])
        print(current_length)
        print
        if current_length > best_length_so_far:
            best_length_so_far = current_length
            best_value = current_value
        # elif current_length == best_length_so_far:
        #     best_value = max(array[0], sub_lis['last_value'])
                
            
    return {'length': best_length_so_far, 'last_value': best_value}


# print(lis([10, 11, 12, 1, 2, 3, 4]))         # length: 4
# print(lis([0, 1, 0, 3, 2, 3]))               # length: 4
# print(lis([10, 9, 2, 5, 3, 7, 101, 18]))     # length: 4
# print(lis([7, 7, 7, 7, 7, 7]))               # length: 1
# print(lis([5, 3, 4]))                        # length: 2

print(lis([11, 12, 1, 2, 3, 4])) 
