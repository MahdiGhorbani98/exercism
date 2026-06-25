"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args) 


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first , second , *rest_of_each_wagons = each_wagons_id
    locomotive , *rest_after_locomotive = rest_of_each_wagons

    final_list = [locomotive ,*missing_wagons, *rest_after_locomotive , first, second]
    return final_list


def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stop_values = list(stops.values())
    x = {'stops':stop_values}
    final_phrase = {**route , **x}
    return final_phrase


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return  {**route,**more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    row_1, row_2, row_3 = wagons_rows
    first_of_row_1, secont_of_row_1, third_of_row_1= row_1
    first_of_row_2, secont_of_row_2, third_of_row_2= row_2
    first_of_row_3, secont_of_row_3, third_of_row_3= row_3

    
    new_row_1 = [first_of_row_1,first_of_row_2 ,first_of_row_3]
    new_row_2 = [secont_of_row_1,secont_of_row_2 ,secont_of_row_3]
    new_row_3 = [third_of_row_1,third_of_row_2 ,third_of_row_3]

    final_list = [new_row_1,new_row_2,new_row_3]
    
    return final_list