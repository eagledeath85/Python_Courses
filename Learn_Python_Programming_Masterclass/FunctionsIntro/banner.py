def banner_text(text, screen_width):
    """
    Get a string and an int.
    The function prints the string centered
    :param text: The text to print
    :param screen_width: The width of the banner
    :return: None
    :raises ValueError: raises an exception if the text is too long
    """
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
