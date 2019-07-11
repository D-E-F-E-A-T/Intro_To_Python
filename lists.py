def even_list(minv, maxv):
    evens = []
    for number in range(minv, maxv):
        if (number % 2) == 0:
            evens.append(number)
    return evens