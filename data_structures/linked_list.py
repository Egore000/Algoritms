from __future__ import annotations
from typing import Any

__doc__ = """
ОДНОНАПРАВЛЕННЫЙ СВЯЗНЫЙ СПИСОК

Массив, где каждый элемент является отдельным объектом и 
состоит из двух элементов – данных и ссылки на следующий узел.

Принципиальным преимуществом перед массивом является 
структурная гибкость: порядок элементов связного списка может не 
совпадать с порядком расположения элементов данных в памяти компьютера, 
а порядок обхода списка всегда явно задаётся его внутренними связями.

Основные операции:

* InsertAtEnd() — Вставка заданного элемента в конец списка,
* InsertAtHead() — Вставка элемента в начало списка,
* Delete() — удаляет заданный элемент из списка,
* DeleteAtHead() — удаляет первый элемент списка,
* Search() — возвращает заданный элемент из списка,
* isEmpty() — возвращает True, если связанный список пуст.

"""


class Node:
    """Узел"""

    @classmethod
    def check_next(cls, link: Node | None):
        if (
            link is not None
            and not isinstance(link, Node)
        ):
            raise ValueError(f"{link!r} is not Node")

    def __init__(self, _data: Any | None = None, _next: Node | None = None):
        self._data = _data
        self.next = _next
    
    def __repr__(self) -> str:
        return repr(f"<{self.__class__.__name__} data={self._data}>")

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data: Any):
        self._data = data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, link: Node | None):
        self.check_next(link)
        self._next = link


class Tools:
    """Дополнительные функции для связного списка"""

    @classmethod
    def get_or_create_node(cls, value: Any) -> Node:
        if isinstance(value, Node):
            return value
        return Node(value)


class LinkedList:
    """Связный список"""

    def __init__(self):
        self._tools = Tools()
        self._head = None

    @property
    def head(self) -> Node | None:
        return self._head

    @head.setter
    def head(self, value: Any):
        self._head = self._tools.get_or_create_node(value)

    def __str__(self):
        output = f"{self._head.data!r}"
        node = self._head.next
        
        while node:
            output += f" -> {node.data!r}"
            node = node.next
        
        return output

    def insert(self, previous: Node, data: Any) -> LinkedList:
        """Вставка узла с данными data после узла previous"""
        node = self._tools.get_or_create_node(data)
        node.next = previous.next
        previous.next = node
        return self

    def insert_at_end(self, data: Any) -> LinkedList:
        """Вставка данных в конец"""
        node = self._tools.get_or_create_node(data)
        tmp = self._head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node
        return self

    def insert_at_head(self, data: Any) -> LinkedList:
        """Вставка данных в начало"""
        node = self._tools.get_or_create_node(data)
        node.next = self._head
        self._head = node
        return self

    def delete(self, data: Any) -> LinkedList:
        """Удаление узла с данными data"""
        tmp = self._head
        if tmp.next:
            if tmp.data == data:
                self.head = tmp.next

            else:
                while tmp.next:
                    if tmp.data == data:
                        break
                    prev = tmp
                    tmp = tmp.next

                if tmp is None:
                    return self

                prev.next = tmp.next
        return self

    def delete_at_head(self):
        """Удаление из начала"""
        self._head = self._head.next

    def is_empty(self):
        """Проверка на пустоту"""
        return self.head is None

    def search(self, key: Any) -> Node | None:
        """Поиск узла с заданным значением"""
        tmp = self._head
        while tmp.next:
            if tmp.data == key:
                return tmp
            tmp = tmp.next
        return None


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = 5
    node = Node(6)
    ll.head.next = node
    ll.insert_at_end('4')
    ll.insert_at_head((1, 3))
    ll.delete('4')
    ll.insert(node, 'hello')
    print(ll)

    print(ll.search(5))
    print(ll.search(8))

    
            