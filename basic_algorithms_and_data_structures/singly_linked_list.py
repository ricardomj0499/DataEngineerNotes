from node import SinglyLinkedNode


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: SinglyLinkedNode = None
        self.tail: SinglyLinkedNode = None

    def append(self, value: int) -> None:
        new_node = SinglyLinkedNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node
            return

    def __iter__(self):
        """
        Defines an iterable of the object
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return (
            " -> ".join(str(value) for value in self) or "Empty List"
        )  # use the iter function inside?

    # Example Usage


def __next__(self):  # Defines how to obtain the next object
    if self._current is None:
        raise StopIteration
    value = self._current.value
    self._current = self._current.next
    return value


lista = SinglyLinkedList()
lista.append(5)
lista.append(4)
lista.append(3)

# Print values using for loop
for x in lista:
    print(x)

# Print list directly
print("List:", lista)

"""
by type constructor

list(my_iterator)

by unpacking

[*my_iterator]

using list comprehension

[e for e in my_iterator]
"""
# Iterate using a for loop
for x in lista:
    print(x)

# Manually using the iterator
it = iter(lista)
print(next(it))  # Outputs: 5
print(next(it))  # Outputs: 4
