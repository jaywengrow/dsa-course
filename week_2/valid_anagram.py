def are_anagrams(first_string, second_string):
    first_word_hash_table = {}
    second_word_hash_table = {}

    for char in first_string:
        if char in first_word_hash_table:
            first_word_hash_table[char] += 1
        else:
            first_word_hash_table[char] = 1

    for char in second_string:
        if char in second_word_hash_table:
            second_word_hash_table[char] += 1
        else:
            second_word_hash_table[char] = 1

    return first_word_hash_table == second_word_hash_table
