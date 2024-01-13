def increment_string(string: str):
    number = ""
    result = ""
    trailing_zeros = 0

    if string.isdigit() or len(string) == 0:
        return str(int(string) + 1) if string.isdigit() else "1"
    else:
        for i in range(len(string)-1, 0, -1):
            if string[i].isdigit():
                if string[i-1] == "0":
                    trailing_zeros += 1
                elif not string[i].isdigit():
                    trailing_zeros = 0
                number += string[i]
            else:
                break

        n = len(number)
        if n != 0:
            string = string[:-n]
            number = int(number[::-1]) + 1
            str_number = str(number)
            if n < len(str_number):
                result += string + ("0" * trailing_zeros) + str_number
            elif n > len(str_number):
                result += string + ("0" * (trailing_zeros-1)) + str_number
            else:
                result += string + str_number
        else:
            result += string + "1"

    return result


print(increment_string("foobar00999"))