"""Various iterable-related boons."""

def iterlog(it, stringifier=str, **kwargs):
    from logging import warning
    for i in it:
        """Log iterable elements as they pass through this node."""
        warning(stringifier(i), **kwargs)
        yield i
