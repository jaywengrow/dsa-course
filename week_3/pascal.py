1. Imagine that the function you’re writing has already been implemented by some other really smart person. It’s all done!
2. Identify the subproblem of the current problem.
3. See what happens when you call the function on the subproblem, and see if there’s enough info for you to answer the current problem.
4. Add the base case!


def recursive_sort():


recursive_sort([5, 3, 8, 1, 0])
recursive_sort([3, 8, 1, 0]) -> [0, 1, 5, 3, 8]
    



def pascal_row(n):
    if n == 1:
        return [1]

    previous_row = pascal_row(n - 1) # -> [1, 3, 3, 1]
    result = [1]

    for i in range(len(previous_row) - 1):
        result.append(previous_row[i] + previous_row[i + 1])
    
    result.append(1)

    return result

# pascal_row(5) -> [1, 4, 6, 4, 1]
# pascal_row(4) -> [1, 3, 3, 1]
#                 [1, 4, 6, 4, 1]
print(pascal(5))
