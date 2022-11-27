
def gen_range(start: int, stop: int, step: int = 1):
    """
    >>> list(gen_range(0, 10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(gen_range(0, 10, 3)) 
    [0, 3, 6, 9]
    >>> list(gen_range(0, 10, -1))
    []
    >>> list(gen_range(10, 0))
    []
    >>> list(gen_range(10, 0, -2))
    [10, 8, 6, 4, 2]
    >>> list(gen_range(-10, -3, 2))
    [-10, -8, -6, -4]
    >>> list(gen_range(0.0, 10))
    Traceback (most recent call last):
    ...
    TypeError
    >>> list(gen_range(0, 10, 0))
    Traceback (most recent call last):
    ...
    ValueError
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()