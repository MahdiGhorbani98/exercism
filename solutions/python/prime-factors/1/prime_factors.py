def factors(value):
    factors_list  = []
    remainder = value
    div = 2
    while remainder > 1:
        if remainder % div  == 0:
            factors_list .append(div)
            remainder = remainder // div
        else:
            div += 1
            
    return factors_list 