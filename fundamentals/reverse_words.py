def reverse_words(text):
    str_list = text.split(" ")
    result = []

    for i in range(0, len(str_list)):
        word_as_list = list(str_list[i])
        word_as_list.reverse()
        reversed_word = "".join(word_as_list)

        if i != len(str_list) -1:
            result.append(reversed_word)
            result.append(" ")
        else:
            result.append(reversed_word)
    
    return "".join(result)

 