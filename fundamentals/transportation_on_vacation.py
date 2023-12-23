def rental_car_cost(d):
    sum = d * 40
    if d >= 7:
        sum -= 50
    elif d >= 3:
        sum -= 20
    return sum
