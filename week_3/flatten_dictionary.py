# See: https://www.geeksforgeeks.org/python-convert-nested-dictionary-into-flattened-dictionary/


def flatten(input, result, parent_key=""):
    if parent_key != "":
        parent_key += "."

    for key, value in input.items():
        if type(value) is dict:
            flatten(value, result, parent_key + key)
        else:
            if parent_key == "":
                result[key] = value
            else:
                result[parent_key + key] = value

    return result


input = {
    "Key1": 1,
    "Key2": {
        "a": 2,
        "b": 3,
        "c": {
            "d": 4,
            "e": {
                "f": 5
            }
        }
    }
}

print(flatten(input, {}))

# Expected result:
# {
#     "Key1": 1,
#     "Key2.a": 2,
#     "Key2.b": 3,
#     "Key2.c.d": 4,
#     "Key2.c.e.f": 5
# }
