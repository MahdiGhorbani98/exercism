def is_pangram(sentence):
    clean_letters = {char.lower() for char in sentence if char.isalpha()}
    
    return len(set(clean_letters)) == 26