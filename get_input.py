def get_user_guess():
    """
    getting the user guess and lower casing it
    :return: user current guess
    :rtype: string
    """
    guess = input("Guess a letter: ")
    guess = guess.lower()
    return guess


def contains_number(value):
    """
    checks if a string contains numbers
    :param value: user guess
    :return: True or False
    """
    for char in value:
        if char.isnumeric():
            return True
    return False


def contains_letter(value):
    """
    checks if a string contains letters
    :param value: user guess
    :return: True or False
    """
    for char in value:
        if char.isalpha():
            return True
    return False


def contains_symbol(value):
    """
    checks if a string contains symbols
    :param value: user guess
    :return: True or False
    """
    for char in value:
        if (not char.isalpha()) and (not char.isnumeric()):
            return True
    return False


def is_valid_input(letter_guessed):
    """
    this func verifies that the user input is only one character and doesn't contain numbers or symbols
    :param letter_guessed: user guess input
    :type: string
    :return: True or False
    :rtype: Boolean
    """
    is_number = contains_number(letter_guessed)
    is_symbol = contains_symbol(letter_guessed)

    if is_number or is_symbol or (len(letter_guessed) > 1) or (len(letter_guessed) < 1):
        print('Your guess has to be one letter only.')
        return False
    else:
        return True
