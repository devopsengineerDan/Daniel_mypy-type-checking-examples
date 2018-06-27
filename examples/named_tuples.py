"""
named_tuples.py
~~~~~~~~~~~~~~~

This modules defines various named tuples, with the aim of
demonstrating best practices for type annotations, as described in the
official documentation for the typing module in the Python standard
library and the mypy docs, for both defining classes and using them
them.
"""

from typing import NamedTuple


class Person(NamedTuple):
    """Basic representation of a person.

    Analagous to examples.classes.Person, but implemented using the
    typing.NamedTuple class and the class-based syntax, as opposed to
    using collections.namedtuple.

    :param first_name: First name.
    :type first_name: str
    :param second_name: Second name.
    :type second_name: str
    :param age: Age.
    :type age: Union[int, float]
    """

    first_name: str
    second_name: str
    age: float


def main() -> None:
    """Executable program.

    Demonstrates how type annotations can be used with class instances.
    """
    
    alex: Person = Person('Alex', 'Ioannides', 38)
    
    msg: str = '{} has been alive for {} years'.format(
        alex.first_name + alex.second_name, alex.age)

    print(msg)
    return None
    