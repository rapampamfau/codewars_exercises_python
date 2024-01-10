def add_binary(a, b):
    sum = a + b
    flag = True
    result = []
    remainder = sum % 2
    to_division = sum // 2

    while flag:
        if to_division == 0:
            flag = False

        result.append(remainder)
        remainder = to_division % 2
        to_division = to_division // 2

    result.append(remainder)
    result.reverse()

    if result[0] == 0:
        result.pop(0)

    return "".join(str(el) for el in result)
