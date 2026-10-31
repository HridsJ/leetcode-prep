def longest_consecutive_subsequence(given_array):
    # removes duplicates and search time is average O(1)
    given_set = set(given_array)
    max_sequence = 0 #tracks the highest recorded sequence until now
    current_sequence = 1
    for num in given_set:
        # if the number is not the beginning of a sequence
        if (num-1) in given_set:
            continue

        # check for consecutive numbers until option exhausted 
        sequence_next = num + 1
        while sequence_next in given_set:
            current_sequence += 1
            sequence_next += 1 
        
        # after options exhausted
        if max_sequence < current_sequence:
            max_sequence = current_sequence
        current_sequence = 1

    return max_sequence

print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))  # Expected: 4
print(longest_consecutive_subsequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Expected: 9
print(longest_consecutive_subsequence([7]))  # Expected: 1
