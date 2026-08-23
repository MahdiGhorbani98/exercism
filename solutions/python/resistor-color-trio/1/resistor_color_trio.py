COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

def label(colors):
    first_two_digit= int(f'{COLORS.index(colors[0])}{COLORS.index(colors[1])}')
    value = first_two_digit * (10** int(COLORS.index(colors[2])))
    final_value = value
    suffix = "ohms"
    if final_value > 0 :
        if final_value % 1000000000 ==0:
            final_value = value / 1000000000
            suffix = "gigaohms"
        elif final_value % 1000000 ==0:
            final_value = value / 1000000
            suffix = "megaohms"
        elif final_value % 1000 ==0:
            final_value = value / 1000
            suffix = "kiloohms"
    else:
        final_value = 0 
        
    return (f'{int(final_value)} {suffix}')