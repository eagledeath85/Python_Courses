# We can provide default values for function parameters
# This way, we can pass only 1 param to the function even if it takes several parameters

def banner_text(text, screen_width=80):
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


banner_text("*")
banner_text(" Always look on the bright side of life")
banner_text("If life seems jolly rotten", 50)
banner_text("And that's to laugh and smile and dance and sing", 80)
banner_text("When you're feeling in the dumps", 50)

print()
print()
print()


def banner_text_2(text=" ", screen_width=66):
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


banner_text_2("*")
banner_text_2(" Always look on the bright side of life")
# We need to pass a keyword argument in the example below
banner_text_2(screen_width=66)
banner_text_2("If life seems jolly rotten", 66)
banner_text_2("And that's to laugh and smile and dance and sing", 66)
banner_text_2("When you're feeling in the dumps", 66)