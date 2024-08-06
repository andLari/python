"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


# Complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_remaining):
    """Calculate the bake time remaining.

    :param time_remaining: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_remaining


# Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(num_of_layers):
    """Calculate the preparation time in minutes.

    :param num_of_layers: int - the number of layers in the lasagna.
    :return: int - preparation time (in minutes).

    Function that takes the number of layers in the lasagna as
    an argument and returns how many minutes it takes to prepare
    the lasagna, assuming each layer takes 2 minutes to prepare.
    """
    return num_of_layers * 2


# Define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_time = preparation_time + elapsed_bake_time
    return total_time
