def is_isogram(phrase):
    
    clean_text = phrase.lower().replace(" ","").replace("-","")
    return len(clean_text) == len(set(clean_text))