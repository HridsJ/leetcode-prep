def two_sum(array_given, target):
    """
    find complement of the current number, check if that complement exists in the map
    if it does then return the index of the number (stored as value) and index of current number
    if not then add current number and its index as current_num:index
    """
    
    search_map = {}
    for i in range(len(array_given)):
        num = array_given[i]
        complement = target - num
        if complement in search_map:
            return [search_map[complement], i]
        search_map[num] = i
    return -1 # if nothing is found
