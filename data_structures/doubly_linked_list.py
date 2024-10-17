from __future__ import annotations

from typing import Any


__doc__ = """
ДВУНАПРАВЛЕННЫЙ СВЯЗНЫЙ СПИСОК

"""


class Node:
    """Узел"""

    def __init__(
            self,
            data: Any,
            previous: Node | None = None,
            _next: Node | None = None
    ):
        self.data = data
        self.prev = previous
        self.next = _next

    def __repr__(self):
        return repr(f"<Node data={self.data}>")


class DoublyLinkedList:
    """Двунаправленный связный список"""

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        node = self.head.next
        output = f"{node.data!r}"

        while node.next != self.tail:
            node = node.next
            output += f" <-> {node.data!r}"

        return output

    @staticmethod
    def insert(data: Any, node: Node) -> Node:
        """Вставка после узла node"""
        tmp = Node(data)
        tmp.prev = node
        tmp.next = node.next
        node.next.prev = tmp
        node.next = tmp
        return tmp

    def insert_at_end(self, data: Any) -> Node:
        """Вставка в конец"""
        return self.insert(data, self.tail.prev)

    def insert_at_head(self, data: Any) -> Node:
        """Вставка в начало"""
        return self.insert(data, self.head)

    def delete(self, value: Node | Any) -> DoublyLinkedList:
        """Удаление"""
        if isinstance(value, Node):
            value.prev.next = value.next
            value.next.prev = value.prev
        else:
            tmp = self.head
            while tmp and (tmp.data != value):
                tmp = tmp.next

            if tmp:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev

        return self


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_head(5)
    dll.insert_at_end(4)
    t = dll.insert(8, dll.head)
    dll.insert(-3, t)

    dll.delete(t)
    print(dll)
