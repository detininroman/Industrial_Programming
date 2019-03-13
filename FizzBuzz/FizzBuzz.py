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

def test_normal():
    """ Normal test.
    """
    arr, output = [1, 2, 3, 5, 15], []
    fizz_buzz(arr, output)
    print (output == [1, 2, 'buzz', 'fizz', 'fizzbuzz'])

def test_big_numbers():
    """ Test with big numbers.
    """
    arr, output = [535555555555, 5500000000000000000000000, 10, 15, 35, 0, -2, -67, -55], []
    fizz_buzz(arr, output)
    print (output == ['fizz', 'fizz', 'fizz', 'fizzbuzz', 'fizz', 'fizzbuzz', -2, -67, 'fizz'])

def test_double():
    """ Test with a fractional number.
    """
    arr, output = [0.1, 0.02, 0.0003], []
    fizz_buzz(arr, output)
    print (output == [0.1, 0.02, 0.0003])

def test_word():
    """ Test with a word.
    """
    arr, output = ['Acronis', 0, 333, 450], []
    fizz_buzz(arr, output)
    print (output == ['Acronis', 'fizzbuzz', 'buzz', 'fizzbuzz'])

def fizz_buzz_test():
    """ Runs all tests.
    """
    test_normal()
    test_big_numbers()
    test_double()
    test_word()

fizz_buzz_test()
