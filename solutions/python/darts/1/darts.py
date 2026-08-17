def score(x, y):
    sum = x**2 + y**2 
    if sum <=1:
        return 10
    elif sum <=25:
        return 5
    elif sum <=100:
        return 1
    return 0