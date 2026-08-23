def rotate(text, key):
    list = []
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                position =ord(letter) - ord('A')
                new_position = (position + key) % 26
                new_letter = chr(new_position + ord('A'))
                list.append(new_letter)
            else:
                position =ord(letter) - ord('a')
                new_position = (position + key) % 26
                new_letter = chr(new_position + ord('a'))
                list.append(new_letter)
        else:
            list.append(letter)
            
    return (''.join(list))