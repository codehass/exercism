def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    else:
        return 2 * square(number - 1)


def total():
    total = 0
    for n in range(1, 65):
        total += square(n) 
    
    return total
