def title_case(title, minor_words=''):
    lower_title_list = title.lower().split(" ")
    minor_words_list = minor_words.lower().split(" ")
    result = ""
    is_equal = False

    for i in range(len(lower_title_list)):

        if i == 0:
            result += lower_title_list[i].capitalize()
        else:

            for minor in minor_words_list:
                if minor != lower_title_list[i]:
                    is_equal = False
                else:
                    is_equal = True
                    break

            if i != len(lower_title_list):

                result += " "
                if is_equal:
                    result += minor
                else:
                    result += lower_title_list[i].capitalize()
    
    return result
