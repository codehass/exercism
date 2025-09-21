def is_armstrong_number(number):
    #  this will return number of digits in the number
    number_of_digits = len(str(number))

    sum_of_powers = 0
    for digit in range(0, number_of_digits):
        sum_of_powers += int(str(number)[digit]) ** number_of_digits

    return sum_of_powers == number

print(is_armstrong_number(154))