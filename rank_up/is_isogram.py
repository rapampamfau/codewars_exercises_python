def is_isogram(string: str):
    string = string.lower()
    for l in string:
        if string.count(l) > 1:
            return False
    return True
