`iterrabble`
============

Various iterable-related functions:

#### `iterlog(it, stringifier=str, **kwargs)`

Logs the elements of an iterable as they are yielded.

#### `iterjoin(join_it, its)`

Joins iterators similarly to str.join.

#### `takemax(it, max)`

Yields a maximum of `max` elements from the iterable `it`.

#### `odometer(source)`

Class instantiator which wraps an iterable,
tracking the count and total size of yields from the wrapped iterable.

Only makes sense around iterables like files which yield sequences.

## Further information

There is more detail provided in the source,
mainly in the form of doctests.

## Considered improvements

    - It may be possible to improve `odometer`
      such that it replaces the `next` method of its wrapped iterator.
      This would enable it to track iteration
      even when the odometer object is not being accessed.

## State

Some function docstrings should explain their variables better.

The API is subject to change in subsequent versions prior to 1.0.

## License

Licensed under the BSD license.
