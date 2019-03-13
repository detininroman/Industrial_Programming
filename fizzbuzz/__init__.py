def is_int(value):
    """ Verifies that 'value' can be converted to an int.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_zero(value):
    """ Compares 'value' with zero.
    """
    return (abs(value - 0.) < 1e-4)


def mul_5(num):
    """ Checks the multiplicity of 5.
    """
    if (is_int(num) == False):
        return False
    return (str(num)[-1] == '0' or str(num)[-1] == '5')


def mul_3(num):
    """ Checks the multiplicity of 3.
    """
    if (is_int(num) == False):
        return False
    if (is_zero(num)):
        return True

    strnum = str(abs(int(num)))
    summary = sum([int(item) for item in list(strnum)])

    if summary in [3, 6, 9]:
        return True
    elif summary in [0, 1, 2, 4, 5, 7, 8]:
        return False
    else:
        return mul_3(summary)


def fizz_buzz(numbers, output):
    """ Matches the list of numbers with the list of expressions.
    """
    for i in numbers:
        if mul_3(i) and mul_5(i):
            output.append('fizzbuzz')
        elif mul_3(i):
            output.append('buzz')
        elif mul_5(i):
            output.append('fizz')
        else:
            output.append(i)
