def is_armstrong_number(number):
    number_string = str(number)
    power = len(number_string)
    total = 0
    for digit in number_string:
        total += int(digit) ** power
        
    return total == number