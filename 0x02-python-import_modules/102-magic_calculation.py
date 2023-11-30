#!/usr/binnpython3
def magic_calculation(a, b):
    result = 0

    if a < b:
        add = __import__('magic_calculation_102').add
        sub = __import__('magic_calculation_102').sub
        result = add(a, b)

        for i in range(4, 6):
            result = add(result, i)

    else:
        result = __import__('magic_calculation_102').sub(a, b)

    return result
