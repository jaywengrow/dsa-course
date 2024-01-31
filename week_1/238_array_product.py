def array_products(array):
    result_array = []
    index = 0
    total_product_so_far = 1
    while index < len(array):
        total_product_so_far *= array[index]
        result_array.append(total_product_so_far)
        index += 1
    
    print(result_array)
    total_product_so_far = 1
    index -= 1

    while index > 0:
        result_array[index] = result_array[index - 1] * total_product_so_far
        print(result_array)
        total_product_so_far *= array[index]
        index -= 1
    
    result_array[0] = total_product_so_far

    return result_array

print(array_products([1, 2, 3, 4])) # [24, 12, 8, 6]
print(array_products([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]