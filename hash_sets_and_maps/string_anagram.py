def string_anagram(given_array):
    """
    Iterate on given array, then take the iteration, use sorted on it
    join the sorted word, and see if it exists in the dictionary we create
    if it exists, then append the original word to the value of the the key you found
    if it does not exist then make it a key with a list that has the original word appended to it
    """

    search_map = {}
    for original_word in given_array:
        sorted_word = "".join(sorted(original_word))
        if sorted_word in search_map:
            search_map[sorted_word].append(original_word)
        else:
            search_map[sorted_word] = [original_word]
    return list(search_map.values())
