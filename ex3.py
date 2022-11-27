def binary_search(elements: list, x) -> bool:
    """
    >>> my_sorted_list = [1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
    >>> binary_search(my_sorted_list, 1)
    True
    >>> binary_search(my_sorted_list, 20) 
    True
    >>> binary_search(my_sorted_list, 21) 
    False
    >>> binary_search(my_sorted_list, "hello") 
    False
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()