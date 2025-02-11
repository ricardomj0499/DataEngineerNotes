from node import SinglyLinkedNode


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: SinglyLinkedNode = None
        self.tail: SinglyLinkedNode = None

    def append(self, value: int) -> None:
        """
        Adds a new node with the given value to the end of the linked list.
        """
        new_node = SinglyLinkedNode(value)
        if not self.head:
            # If the list is empty, set both head and tail to the new node.
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current tail and update the tail.
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_beginning(self, value: int):
        """Inser value at the very beginnning"""
        pass

    def del_value(self, Value: int):
        """Del first element of list that finds with value"""
        pass

    def del_index(self, index: int):
        """del from index"""
        pass

    def pop(self):
        """del from the end"""
        pass

    def __iter__(self):
        """
        Defines an iterable for the linked list using a generator.
        No need to implement __next__ separately as yield manages state.
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    '''
    def __iter__(self):
        """
        Alternative iterator implementation.
        Requires a separate __next__ function to define how elements are retrieved.
        """
        self._current = self.head  # Track the current node during iteration.
        return self

    def __next__(self):
        """
        Defines how to obtain the next element for the custom iterator.
        Raises StopIteration when the end of the list is reached.
        """
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value
    '''

    def __str__(self):
        """
        Provides a string representation of the linked list.
        Uses the generator in __iter__ to traverse elements.
        """
        return " -> ".join(str(value) for value in self) or "Empty List"


# Example usage
lista = SinglyLinkedList()
lista.append(5)
lista.append(4)
lista.append(3)
lista.append(2)
lista.append(1)

# Iterate using a for loop
print("List elements (for loop):")
for x in lista:
    print(x)

# Print the entire list directly
print("List representation:", lista)

# Use case 2: Manually using an iterator
iterator = iter(lista)
print("Manual iteration:")
print(next(iterator))  # Outputs: 5
print(next(iterator))  # Outputs: 4
print(next(iterator))  # Outputs: 3

# Additional TODOs:
# Uncomment and test the following use cases:
# 1. Type constructor conversion to list
print("As list:", list(iterator))

# 2. Unpacking with * operator
print("Unpacked elements:", [*lista])

# 3. List comprehension
print("List comprehension result:", [e for e in lista])
