def square_of_sum(number):
    total = 0
    
    for i in range(number):
        total += i+1
    
    total = total ** 2 
    return total


def sum_of_squares(number):
    total = 0
    
    for i in range(number):
        total += (i+1)**2
    
    
    return total


def difference_of_squares(number):
    total = square_of_sum(number) - sum_of_squares(number)
    return total