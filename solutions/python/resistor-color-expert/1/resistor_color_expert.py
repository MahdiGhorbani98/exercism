COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
TOLERANCE ={"grey" : "0.05%","violet" : "0.1%","blue" : "0.25%","green" : "0.5%","brown" : "1%","red" : "2%","gold" : "5%","silver" : "10%",}

def resistor_label(colors):
    main_value = 0
    suffix = "ohms"
     
    if len(colors) == 1 :
        return "0 ohms"
        
        
    elif len(colors) == 4:
        main_value  = int(f'{COLORS.index(colors[0])}{COLORS.index(colors[1])}') * (10**COLORS.index(colors[2]))
        return f'{suffix_generator(main_value)} ±{TOLERANCE[colors[3]]}'
        
        
    elif len(colors) == 5:
        main_value  = int(f'{COLORS.index(colors[0])}{COLORS.index(colors[1])}{COLORS.index(colors[2])}') * (10**COLORS.index(colors[3]))
        return f'{suffix_generator(main_value)} ±{TOLERANCE[colors[4]]}'
        
def suffix_generator(value):
    final_value = value
    suffix = "ohms"
    if final_value >= 1000000000:
        final_value = value / 1000000000
        suffix = "gigaohms"
    elif final_value >= 1000000:
        final_value = value / 1000000
        suffix = "megaohms"
    elif final_value >= 1000:
        final_value = value / 1000
        suffix = "kiloohms"

    if final_value == int(final_value):
        final_value = int(final_value)

    return f'{final_value} {suffix}'

