def bouncing_ball(h, bounce, window):
    result = 0
    if h > 0 and h > window and 1 > bounce > 0:
        while(True):
            result += 1
            h = h*bounce
            if h > window:
                result += 1
            else:
                break
        return result

    else:
        return -1
