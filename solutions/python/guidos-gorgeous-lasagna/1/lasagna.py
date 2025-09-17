EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time

    :param elapsed_bake_time: int - the elapsed bake time
    :return: int - the remaining time

    This function take one parameter representing elapsed bake time and calculate 
    the difference between EXPECTED BAKE TIME and elapsed bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

PREPARATION_TIME = 0

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time

    :param number_of_layers: int - the number of layers
    :return: int - total preparation time in minutes

    This function takes one parameter number of layers and return the preparation time in minutes
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return 2 * number_of_layers + elapsed_bake_time

