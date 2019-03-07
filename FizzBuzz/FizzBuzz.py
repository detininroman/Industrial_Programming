def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_zero(value):
    return (abs(value - 0.) < 1e-4)

def mul_5(num):
    if (is_int(num) == False):
        return False
    return (str(num)[-1] == '0' or str(num)[-1] == '5')

 def mul_3(num):
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

 def test_normal():
    arr, output = [1, 2, 3, 5, 15], []
    fizz_buzz(arr, output)
    print (output == [1, 2, 'buzz', 'fizz', 'fizzbuzz'])

def test_big_numbers():
    arr, output = [535555555555, 5500000000000000000000000, 10, 15, 35, 0, -2, -67, -55], []
    fizz_buzz(arr, output)
    print (output == ['fizz', 'fizz', 'fizz', 'fizzbuzz', 'fizz', 'fizzbuzz', -2, -67, 'fizz'])

def test_double():
    arr, output = [0.1, 0.02, 0.0003], []
    fizz_buzz(arr, output)
    print (output == [0.1, 0.02, 0.0003])

def test_word():
    arr, output = ['Acronis', 0, 333, 450], []
    fizz_buzz(arr, output)
    print (output == ['Acronis', 'fizzbuzz', 'buzz', 'fizzbuzz'])

test_normal()
test_big_numbers()
test_double()
test_word()        