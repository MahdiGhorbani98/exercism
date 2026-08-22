def is_valid(isbn):
    formatted_isbn = isbn.replace("-","") 
    formatted_isbn_len = len(formatted_isbn)
    
    total = 0
    
    if formatted_isbn_len == 10:
        for i in range(formatted_isbn_len):
            if i < 9:
                if formatted_isbn[i].isdigit():
                    total += int(formatted_isbn[i]) * (10-i)
                else:
                    return False
            if i == 9:
                if formatted_isbn[i] == 'X':
                    total += 10
                elif formatted_isbn[i].isdigit():
                    total += int(formatted_isbn[i])
                else: 
                    return False
        return total % 11 == 0
    
            
    return False
        


