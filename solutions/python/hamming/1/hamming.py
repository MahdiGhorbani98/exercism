def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    total_dif = 0
    
    for char_a, char_b in zip(strand_a,strand_b):
        if char_a != char_b:
            total_dif +=1
            
    return total_dif