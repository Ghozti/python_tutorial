def get_max(num_list):
    current_max = num_list[0]
    for num in num_list:
        if current_max < num:
            current_max = num
    return current_max
