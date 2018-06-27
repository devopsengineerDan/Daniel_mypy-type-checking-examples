"""
classes.py
~~~~~~~~~~

This modules define a simple classe, with the aim of
demonstrating best practices for type annotations, as described in the
official documentation for the typing module in the Python standard
library and the mypy docs, for both defining classes and using them
them.
"""

from typing import Union


class Person:
    """Basic representation of a person.

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

    def __init__(self, first_name: str, second_name: str,
                 age: Union[int, float]) -> None:

        self.first_name = first_name
        self.second_name = second_name
        self.age = float(age)

    def decades_old(self) -> int:
        return int(self.age // 10)
        

def main() -> None:
    """Executable program.

    Demonstrates how type annotations can be used with class instances.
    """
    
    alex: Person = Person('Alex', 'Ioannides', 38)
    
    msg: str = '{} has been alive for {} decades'.format(
        alex.first_name, alex.decades_old())

    print(msg)
    return None
