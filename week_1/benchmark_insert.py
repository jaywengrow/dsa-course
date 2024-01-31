import timeit

test_code = ''' 
array = []
for i in range(1000000):
    array.insert(len(array), i)
'''

print(timeit.timeit(stmt=test_code, number=1))
