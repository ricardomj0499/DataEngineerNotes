# Node class with only a integer value for now


class SinglyLinkedNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: SinglyLinkedNode = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"SinglyLinkedNode(Value={self.value})"
