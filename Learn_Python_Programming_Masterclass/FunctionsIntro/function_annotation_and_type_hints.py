# We can specifiy in the function definition what type the parameters are
# and what the type the function returns
# Syntax is like this: def function_name(param1: type, param2: type) -> return type

def multiply_arguments(x: float, y: float) -> float:
    """
    Get 2 values from Standard Input (stdint).
    The function multiplies the 2 values passed
    :param x: first parameter. Can be `int`, `double` or `float`
    :param y: second parameter. Can be `int`, `double` or `float`
    :return: The product of `x` multiplied by `y`
    """
    result = x * y
    return result


# We can also specify the type of the parameters even when they have default values
# Syntax is def function_name(param1: type = default_value, param2: type = default_value) -> return type
def banner_text(text: str = " ", screen_width: int = 80) -> None:
    # screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
        # print("The text is too long to fit in the specified width")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*", 80)
banner_text(" Always look on the bright side of life", 80)
banner_text("If life seems jolly rotten", 80)
banner_text("And that's to laugh and smile and dance and sing", 80)


multiply_arguments()