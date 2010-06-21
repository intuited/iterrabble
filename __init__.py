"""Various iterable-related boons."""

def iterlog(it, stringifier=str, **kwargs):
    """Log iterable elements as they pass through this node.
    
    >>> import logging
    >>> import sys
    >>> loghandler = logging.StreamHandler(sys.stdout)
    >>> logger = logging.getLogger()
    >>> logger.addHandler(loghandler)
    >>> noisemaker = ('noise: {0}'.format(i) for i in range(2))
    >>> noiselogger = iterlog(noisemaker)
    >>> noise_fan = ('I like {0}'.format(i) for i in noiselogger)
    >>> print noise_fan.next()
    noise: 0
    I like noise: 0
    >>> print noise_fan.next()
    noise: 1
    I like noise: 1
    """
    from logging import warning
    for i in it:
        warning(stringifier(i), **kwargs)
        yield i


def iterjoin(join_it, its):
    """Joins iterators similarly to str.join.
    
    >>> list(iterjoin('', ('one', 'two')))
    ['o', 'n', 'e', 't', 'w', 'o']
    >>> ''.join(iterjoin('_', ('^', '', '^')))
    '^__^'
    >>> list(iterjoin((10, ), [(1, 2, 3), (4, 5, 6)]))
    [1, 2, 3, 10, 4, 5, 6]
    >>> list(iterjoin('_', ''))
    []
    """
    from itertools import chain, izip, repeat
    its = iter(its)
    join_tuple = tuple(join_it)

    # # This is the 'conventional' version using for and yield.
    # # It works but is theoretically slower.
    # for i in its.next():
    #     yield i
    # for it in its:
    #     for i in join_it:
    #         yield i
    #     for i in it:
    #         yield i

    try:
        its_first = its.next()
    except StopIteration:
        # This is the case where `its` is initially empty.
        return iter(())

    its_after_first = chain.from_iterable(izip(repeat(join_tuple), its))
    joined_its = chain((its_first,), its_after_first)
    iterated_joined_its = chain.from_iterable(joined_its)
    return iterated_joined_its
