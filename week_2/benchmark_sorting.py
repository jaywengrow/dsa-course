import timeit

setup_code = '''
import random

array = []
for i in range(100000):
    n = random.randint(1, 100000)
    array.append(n)
'''


test_code = ''' 
array.sort()
'''

print(timeit.repeat(stmt=test_code, setup=setup_code, repeat=5, number=1))