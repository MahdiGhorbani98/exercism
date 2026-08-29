def egg_count(display_value):
    dividend = display_value
    total = 0
    
    while dividend > 0:
        remainder = dividend % 2
        dividend = dividend // 2
        if(remainder == 1):
            total += 1
            
    return total