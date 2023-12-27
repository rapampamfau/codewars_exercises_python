def spin_words(sentence):
    sentence_l = sentence.split(" ")
    result = []
    for word in sentence_l:
        if len(word) >= 5:
            result.append(reverse_word(word))
        else:
            result.append(word)
    return " ".join(result)
            

def reverse_word(word: str):
    word_l = list(word)
    word_l.reverse()
    return "".join(word_l)
