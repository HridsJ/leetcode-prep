def valid_palindrome(given_string):
    given_string = given_string.lower()
    string_length = len(given_string)
    left_ptr = 0
    right_ptr = string_length-1
    while right_ptr > left_ptr:
        while (given_string[right_ptr].isalnum() == False) and right_ptr > left_ptr:
                    right_ptr -= 1
        while (given_string[left_ptr].isalnum()==False) and right_ptr > left_ptr:
                    left_ptr += 1
        if given_string[left_ptr] != given_string[right_ptr]:
            return False
        right_ptr -= 1
        left_ptr += 1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))