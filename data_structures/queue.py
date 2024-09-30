from __future__ import annotations
from typing import Iterable, Any


__doc__ = """
ОЧЕРЕДЬ

Подобно стекам, хранит элементы последовательным образом.

Отличие от стека - использование FIFO (First In Fisrt Out) 
вместо LIFO (Last In First Out)

Основные операции: 
* Enqueue() — вставляет элемент в конец очереди,
* Dequeue() — удаляет элемент из начала очереди,
* isEmpty() — возвращает значение true, если очередь пуста,
* Top() — возвращает первый элемент очереди.
"""


class Queue:
    """Очередь (FIFO)"""

    @classmethod
    def check_iterable(cls, item: Any):
        """Проверка на итерируемость"""
        if not issubclass(item.__class__, Iterable):
            raise ValueError(f"{item} is not iterable!")

    def __init__(self, data: Iterable[Any] | None = None):
        self.data = data

    def __repr__(self):
        return repr(self.__data)
    
    @property
    def data(self) -> Iterable[Any]:
        return self.__data
    
    @data.setter
    def data(self, _data: Iterable[Any] | None):
        if _data is None:
            self.__data = []
            return 
        
        self.check_iterable(_data)
        
        if len(_data) == 0:
            self.__data = []
        else:
            self.__data = _data
        
    def enqueue(self, item: Any) -> Queue:
        """Добавление в конец"""
        self.__data.append(item)
        return self
    
    def dequeue(self) -> Queue:
        """Удаление из начала"""
        self.__data.pop(0)
        return self
    
    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return not bool(self.__data)
    
    def top(self) -> Any | None:
        """Первый элемент в очереди"""
        if not self.is_empty():
            return self.__data[0]
        return None
        

if __name__ == "__main__":
    q = Queue([1, 2, "Abc", (1, 4)])
    q.enqueue(10)
    q.dequeue().dequeue()
    print(q)

    q1 = Queue()
    print(q1.top())
