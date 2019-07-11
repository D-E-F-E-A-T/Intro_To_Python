def partition(number):
    if (number % 2) == 0:
        my_tup = (number, None)
        return my_tup
    else:
        my_tup = (None, number)
        return my_tup
    
def partition_list(numbers):
    evens = []
    odds = []
    
    for number in numbers:
        tup = partition(number)
        evens.append(tup[0])
        odds.append(tup[1])
    
    final = (evens, odds)
    return final
        
        