def max_avg_subarray(nums, k):
    i = 0
    j = i + k

    window_sum = sum(nums[i:j])
    max_avg = window_sum/k
    new_sum = window_sum

    while j < len(nums):
        new_sum -= nums[i]
        # not j+1 because j here represents the end of the window as a posiiton not index
        # since i+k made k=4 pointing to element 5
        new_sum += nums[j]
        i += 1
        j += 1        
        new_avg = new_sum / k

        if new_avg > max_avg:
            max_avg = new_avg
    return max_avg

