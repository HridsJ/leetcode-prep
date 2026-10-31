def most_water(heights):
    """
    in the array heights, take two pointers r and l, write code to maximize
        (r-l)*min(r, l)

    take two pointers on right and left, while right > left, keep moving
    calculate area between them and track that in a variable called maximum
    then move the one with lower value (not the index, but the value at that index in heights)
    """
    max_area = 0
    left_ptr = 0
    right_ptr = len(heights) - 1
    while left_ptr < right_ptr:
        current_area = (right_ptr - left_ptr) * min(heights[right_ptr], heights[left_ptr])
        if current_area > max_area:
            max_area = current_area
        if heights[right_ptr] > heights[left_ptr]:
            left_ptr += 1
        else:
            right_ptr -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(most_water(height))