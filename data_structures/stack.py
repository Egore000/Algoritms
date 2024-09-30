from __future__ import annotations
from typing import Iterable, Any

__doc__ = """
СТЕК

Абстрактный тип данных, представляющий собой список элементов, 
организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

Основные операции:

* Push() - вставляет элемент сверху,
* Pop() - возвращает верхний элемент после удаления из стека,
* isEmpty() - возвращает true, если стек пуст,
* Top() - возвращает верхний элемент без удаления из стека.
"""

class Stack:
    """Стек (LIFO)"""
    
    @classmethod
    def check_iterable(cls, item: Iterable[Any]):
        if not issubclass(item.__class__, Iterable):
            raise ValueError(f"{item} is not iterable!")

    def __init__(self, data: Iterable[Any] | None = None):
        self.data = data

    def __repr__(self):
        return repr(self.__data)

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: Iterable[Any] | None):
        if data is None:
            self.__data = []
            return
        
        self.check_iterable(data)

        if len(data) == 0:
            self.__data = []
            return
        
        self.__data = data

    def push(self, item) -> Stack:
        """Добавление наверх"""
        self.__data.insert(0, item)
        return self
    
    def pop(self) -> Any:
        """Удалить и вернуть элемент сверху"""
        return self.__data.pop(0)
    
    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return not bool(self.__data)
    
    def top(self) -> Any:
        """Верхний элемент без удаления"""
        return self.__data[0]
    

if __name__ == "__main__":
    s = Stack([1, "LIFO", (1,)])
    print(s)
    el = s.pop()
    print(el, s)

    s.push(12).push("ABC")
    print(s)