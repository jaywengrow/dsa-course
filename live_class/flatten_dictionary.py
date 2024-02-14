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

def flatten(input_hash, flat_hash, parent_key_name):
    flat_hash = {"Key1": 1, "a": 2, "b": 3, "d": 4, "f": 5}
    current_name = parent_key_name + current_key_name
    if value is not a dict,    
        add the  and value to flat_hash
    else: # it IS a dict
        flatten(value, flat_hash, current_name)




print(flatten(input, {}))

# Expected result:
# {
#     "Key1": 1,
#     "Key2.a": 2,
#     "Key2.b": 3,
#     "Key2.c.d": 4,
#     "Key2.c.e.f": 5
# }