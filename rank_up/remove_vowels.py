def disemvowel(string_):
    new_string = ""
    for char in string_:
        if not is_vowel(char):
            new_string += char

    return new_string


def is_vowel(char):
    for vowel in "aeiouAEIOU":
        if char == vowel:
            return True
    return False
