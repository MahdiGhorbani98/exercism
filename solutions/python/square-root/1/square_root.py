def square_root(number):
    low = 1
    high = number 
    while low <= high:
        middle = (low + high) // 2
        if middle*middle == number:
            return middle
        elif middle*middle < number:
            low = middle +1
        else:
            high = middle -1