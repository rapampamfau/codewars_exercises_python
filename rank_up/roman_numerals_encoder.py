def solution(n):
    n_as_list = list(str(n))
    result = ""
    
    for i in range(len(n_as_list)):
        str_num = f"{n_as_list[i]}{(len(n_as_list) - 1 - i) * '0'}"
        num = int(str_num)

        if len(str_num) == 4:
            num = num // 1000
            if 0 < num <= 3:
                result += num * "M"

        elif len(str_num) == 3:
            num = num // 100
            if 0 < num <= 3:
                result += num * "C"
            if 3 < num < 5:
                result += "CD"
            elif num == 5:
                result += "D"
            if 5 < num < 9:
                diff = num - 5
                result += "D" + diff * "C"
            if 8 < num < 10:
                diff = 10 - num
                result += diff * "C" + "M"

        elif len(str_num) == 2:
            num = num // 10
            if 0 < num <= 3:
                result += num * "X"
            if 3 < num < 5:
                result += "XL"
            elif num == 5:
                result += "L"
            if 5 < num < 9:
                diff = num - 5
                result += "L" + diff * "X"
            if 8 < num < 10:
                diff = 10 - num
                result += diff * "X" + "C"

        elif len(str_num) == 1:
            if 0 < num <= 3:
                result += num * "I"
            if 3 < num < 5:
                result += "IV"
            elif num == 5:
                result += "V"
            if 5 < num < 9:
                diff = num - 5
                result += "V" + diff * "I"
            if 8 < num < 10:
                diff = 10 - num
                result += diff * "I" + "X"

    return result
