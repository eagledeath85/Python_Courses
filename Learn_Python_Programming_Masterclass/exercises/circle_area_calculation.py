import math


def circle_area(radius: float) -> float:
    """
    Calculates the circle area of a given radius
    :param radius: the circle radius
    :return: the circle area
    """
    area = math.pi * radius * radius
    return area


radius_input_from_user = float(input("Please enter a radius: "))
result = circle_area(radius_input_from_user)
print("The area of a circle of radius {0} is {1}".format(radius_input_from_user, str(result)))