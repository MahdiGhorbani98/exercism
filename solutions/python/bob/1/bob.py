def response(hey_bob):
    normalizeInput = hey_bob.strip()
    if len(normalizeInput) == 0:
        return "Fine. Be that way!"
    
    if normalizeInput.endswith("?"):
        if normalizeInput.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if normalizeInput.isupper():
        return "Whoa, chill out!"
        
    return "Whatever."