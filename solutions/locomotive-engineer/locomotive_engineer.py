"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    x, y, z, *last = each_wagons_id
    return [z] + missing_wagons + last + [x] + [y]

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    existing_stops = route.get("stops", [])

    new_stops = []
    
    for stop in kwargs.values():
        new_stops.append(stop)

    route["stops"] = existing_stops + new_stops
    
    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route
    


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    row1, row2, row3 = wagons_rows

    new_row1 = [row1[0], row2[0], row3[0]]
    new_row2 = [row1[1], row2[1], row3[1]]
    new_row3 = [row1[2], row2[2], row3[2]]


    return [new_row1, new_row2, new_row3]
