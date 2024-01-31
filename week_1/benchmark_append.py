import timeit

test_code = ''' 
array = []
for i in range(10000000):
    array.append(i)
'''

print(timeit.timeit(stmt=test_code, number=1))
