"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return (EXPECTED_BAKE_TIME - elapsed_bake_time)


def preparation_time_in_minutes(number_of_layers):
    """ Calculate the preparation time based on the amount of layers.

    Parameters:
        number_of_layers(int): The number of layers the lasagna shall have.

    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers the lasagna shall have and returns
    how many minutes it will take to prepare based on 'PREPARATION_TIME'.
    """
    
    return (PREPARATION_TIME * number_of_layers)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time cooking the lasagna.

    Parameters:
        number_of_layes(int): The number of layers added to the lasagna.
        elapsed_bake_time(int): The number of minutes the lasagna has spent baking
        in the oven already.

    Returns:
        int: The total minutes spent in the kitchen cooking.

    Function that takes the preparation time layering and the time the lasagna has spent
    baking in the oven and returns the total minutes you have been in the kitchen cooking.
    """

    preparation = preparation_time_in_minutes(number_of_layers)
    return (preparation + elapsed_bake_time)
