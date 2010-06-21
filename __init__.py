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
