# Only shows some docstrings attributes


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """


print(my_function.__doc__)


def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs


f("spam")
