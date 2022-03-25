def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    #solution does not account for negative numbers
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
