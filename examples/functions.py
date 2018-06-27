"""
functions.py
~~~~~~~~~~~~

This modules define various simple function, with the aim of
demonstrating best practices for type annotations, as described in the
official documentation for the typing module in the Python standard
library and the mypy docs.
"""

from typing import Union, List, TypeVar, Sequence, Callable, Any, Optional


def add(x: float, y: float) -> float:
    """Add two numbers.

    In this instance, we are assuming that the function will be used
    with variable of type `float` and that the return will therefore also
    be a `float`. This is, however, ambiguous, as the function would also
    work with `int`. A better solution would be to define a type
    varable and restrict it to `float` and `int`.

    Perhaps a more pythonic approach would be to 'relax' about the
    possibility of having an `int` as an argument as oppossed to a
    `float`, as duck typing enables `int` to be valid whenever a
    `float` is expected.
    
    :param x: An arbitrarty number.
    :type x: float
    :param y: An arbitrarty number.
    :type y: float
    :return: The sum of two numbers.
    :rtype: float
    """

    z: float = x + y
    return z


def area_of_circle(radius: float) -> float:
    """Compute the area of a circle.
    
    Another simple example that demonstrates that it isn't necessary to
    annotate the types of local variables in order to be able to
    type-check the output stated type of a function, given the input
    types. This demonstrates how the type annotation system can be used
    for defining and enforcing interfaces, etc.

    :param radius: Circle radius in aribrary units.
    :type radius: float
    :return: The area of the circle.
    :rtype: float
    """

    from math import pi

    return pi * (radius ** 2)


def area_of_semicircle(radius: float) -> float:
    """Compute the area of a semi-circle.

    Reinforces the points made above, regarding the enforcement of
    interfaces/contracts and not needing to annote types 'in-bewtween',
    when they can be inferred from the input types, etc.
    
    :param radius: Circle radius in aribrary units.
    :type radius: float
    :return: The area of the semi-circle.
    :rtype: float
    """

    return area_of_circle(radius) / 2


def divide(x: Union[int, float], y: Union[int, float]) -> float:
    """Divide two numbers.

    In this instance we are not making any assumptions as to whether or
    not the arguments are `float` or `int`. Instead, we use a `Union`
    of default types to describe the ambiguity, which we then resolve
    explicitly before we return. 
    
    Hypothetically, we could also return a `Union[int, float]`, but
    this bad practice as it perpetuates ambiguity that have to be resolved
    downstream at some point - either with explicit type conversion (as
    below), using `typing.cast` or by conditioning control flow using
    `isinstanceof()` to narrow-down the type options. 

    Also, there is currently a bug in mypy that means it cannot resolve
    the potential types for arithmetic operators of `Union` types and so
    it cannot automaticaly identify the return type can only be a 
    `float`.
    
    :param x: An arbitrarty number.
    :type x: Union[int, float]
    :param y: An arbitrarty number.
    :type y: Union[int, float]
    :return: The product of the function arguements.
    :rtype: float
    """
    
    return float(x) / y


Q = TypeVar('Q', float, int)

def sum_squares(numbers: Sequence[Q]) -> Q:
    """Compute the sum of the squares of a sequence of numbers.

    Best practice, according to the documentation for the typing
    module, is not to specify the precise type of collection as the
    function arguement, but rather the protocol type of the collection
    that the function can work with and the generic type of the
    sequence, defined by a type variable that is restricted to being a
    `float` or an `int`.
    
    Note, this is not an alternative to using `Union`, that allows for
    differing types in the input sequence and return variables. 
    Instead, using a type variable forces the parametrisiation to be a
    single type.
    
    :param numbers: A sequence of numbers - e.g. a collection, c, for
        which `isinstance(c, collections.abc.Sequence) = True`.
    :type numbers: Sequence[Q]
    :return: A number representing the sum of the square of the input
        sequence.
    :rtype: Q
    """

    return sum(num ** 2 for num in numbers)


def mapper(numbers: Sequence[Q], 
           f: Callable[[Q], Q]) -> List[Q]:
    """Apply a function to a sequence of numbers.
    
    An alternative for the builtin `map` function. As for the 
    `sum_squares` function, but this time we define the precise type
    collection that the function returns, as we know with certainty
    what it will be.

    :param numbers: A sequence of numbers - e.g. a collection, c, for
        which isinstance(c, collections.abc.Sequence) = True.
    :type numbers: Sequence[Q]
    :param f: A unary function that maps a number to a number.
    :type f: Callable[[Q, Q], Q]
    :return: The input sequence after having been transformed by f.
    :rtype: List[Q]
    """

    return list(f(num) for num in numbers)


def to_stdout(x: Any, msg: Optional[str] = None) -> None:
    """Print an object to std out.

    This is the same the builtin `print` funtion, that demonstrates 
    how the `Any` type can be used as an 'escape hatch' for a dynamic
    type and how the `Optional` type can be used as an alternative to
    `Untion[str, None]`.

    Note, that it is best practice to explicity define `None` as a
    return and return type for function that are used only for their
    side effects.
    
    :param x: An arbitrary object.
    :type x: Any
    :param msg: Optional message to display first, defaults to None.
    :param msg: Optional[str], optional
    :return: Nothing.
    :rtype: None
    """

    if (msg):
        print(msg)

    print(x)
    return None
