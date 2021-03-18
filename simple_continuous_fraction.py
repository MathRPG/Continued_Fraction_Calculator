import math


def split_integer_and_decimal_parts(value):
    rounded_value = round(value)
    if math.isclose(value, rounded_value):
        return rounded_value, 0

    integer_part = math.floor(value)
    return integer_part, value - integer_part


def simple_continuous_fraction(value, depth=10):
    # TODO: specify that output is in latex; maybe make array return later?
    integer, decimal = split_integer_and_decimal_parts(value)
    result = str(integer)

    if not math.isclose(decimal, 0) and depth > 1:
        result += ' + \\dfrac{1}{%s}' % simple_continuous_fraction(1 / decimal, depth - 1)

    return result
