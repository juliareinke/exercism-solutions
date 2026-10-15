"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    list_wagon = list(args)
    return list_wagon


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first, second, third, *remain = each_wagons_id
    *corrected_wagons, = third, *missing_wagons, *remain, first, second
    return corrected_wagons


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops = list(kwargs.values())
    updated_route = {**route, "stops":stops}
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_info = {**route, **more_route_information}
    return extended_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    [[*first],[*second],[*third]] = wagons_rows
    separated_rows = [list(first), list(second), list(third)]
    new_first, new_second, new_third = zip(*separated_rows)
    fixed_depot = [[*new_first], [*new_second], [*new_third]]
    return fixed_depot
