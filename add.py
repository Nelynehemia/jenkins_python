import numbers


def adding(x, y):
    if isinstance(x, numbers.Number) & isinstance(y, numbers.Number):
        return x + y
    else:
        raise TypeError("one or more of the arguments is not a number")
