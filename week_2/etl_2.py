def etl2(data):
    output = {}

    for key, values in data.items():
        for value in values:
            output[value.lower()] = key

    return output


input = {
    1: ["A", "E"],
    2: ["D", "G"]
}

print(etl2(input))

# expected output:
# {
# 'a': 1,
# 'd': 2,
# 'e': 1,
# 'g': 2
# }

