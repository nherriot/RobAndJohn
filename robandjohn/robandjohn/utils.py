# Helper functions used within the program


def unpack_list(list_):
    """
    Get (single) element from list.

    Examples
    --------
    >>> unpack_list(['foo'])
    'foo'
    """
    (element,) = list_
    return element
