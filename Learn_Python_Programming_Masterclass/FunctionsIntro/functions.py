# Syntax of a function is
# def function_name(arguments):
def multiply():
    result = 10.5 * 4
    return result


answer = multiply()
print(answer)


def multiply_arguments(x, y):
    """
    Get 2 values from Standard Input (stdint).
    The function multiplies the 2 values passed
    :param x: first parameter. Can be `int`, `double` or `float`
    :param y: second parameter. Can be `int`, `double` or `float`
    :return: The product of `x` multiplied by `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Get a String from Standard Input (stdint)
    The function reverts the String entered by the user and checks if it is a palindrome
    :param string: The String to check
    :return: `True` if the reversed String is equal to the original String
        `False` otherwise
    """
    # To check if a word is a palindrome, we can reverse it and check if it is equal to the original word
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


def palindrome_sentence_from_udemy(sentence_udemy):
    """
    Get a String from Standard Input (stdint)
    The function reverts a sentence and checks if it is a palindrome
    :param sentence_udemy: The sentence to check
    :return: `True` if the reversed sentence is equal to the original sentence
        `False` otherwise
    """
    string = ""
    for char in sentence_udemy:
        if char.isalnum():
            string += char
    #return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

def is_palindrome_sentence(sentence_input):
    """
    Get a String from Standard Input (stdint)
    :param sentence_input: The sentence to check
    :return: `True` if the reversed sentence is equal to the original
        `False` otherwise
    """
    separators = ""
    for character in sentence_input:
        if not character.isalnum():
            separators = separators + character
    words_from_sentence = "".join(
        character if character not in separators else " " for character in sentence_input).split()
    letters_from_sentence_list = []
    letters_string = ""
    for word in words_from_sentence:
        for letter in word:
            letters_from_sentence_list.append(letter)
    for letter in letters_from_sentence_list:
        letters_string += letter
    backwards = letters_string[::-1]
    if letters_string.casefold() == backwards.casefold():
        return True
    else:
        return False


def fibonnaci(n: int) -> int:
    """Return the `n` th Fibonnaci number, for positive `n` ."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for fib in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result

sentence = "Was it a car, or a cat, I saw?"
if is_palindrome_sentence(sentence):
    print("The sentence '{0}' is a palindrome".format(sentence))
else:
    print("The sentence '{0}' is not a palindrome".format(sentence))

print("*" * 40)

if palindrome_sentence_from_udemy(sentence):
    print("The sentence '{0}' is a palindrome".format(sentence))
else:
    print("The sentence '{0}' is not a palindrome".format(sentence))

word = input("Please enter your word: ")
if is_palindrome(word):
    print("The word {} is a palindrome".format(word))
else:
    print("The word {} is a not palindrome".format(word))

answer = multiply_arguments(3, 4)
print(answer)
print()

for val in range(1, 10):
    two_times = multiply_arguments(2, val)
    print(two_times)

for i in range(36):
    print(i, fibonnaci(i))

multiply_arguments()