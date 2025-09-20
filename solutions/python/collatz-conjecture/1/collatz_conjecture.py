def steps(number):
    # if it's even divide it by 2
    # if it's odd multiple it by 3 and add 1

    # objective of the function is to return the number of steps to reach 1 according to the rules of the Collatz Conjecture
    
    number_of_steps = 0
    if number <= 0 :
        raise ValueError("Only positive integers are allowed")

    while number > 1:
        if number % 2 == 0:
            number = number /2
            number_of_steps += 1
        else:
            number = number * 3 + 1
            number_of_steps += 1
    
    return number_of_steps
