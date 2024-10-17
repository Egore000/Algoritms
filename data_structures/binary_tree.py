from __future__ import annotations
from numbers import Number


__doc__ = """
БИНАРНОЕ ДЕРЕВО ПОИСКА

Дерево — это структура, данные в которой лежат в узлах. 
У каждого узла могут быть один или несколько дочерних и только один родитель,
то есть они расходятся, как ветви дерева:
                    
                    10
                  /   \
                 5    13
               /  |     \
              3   7     19
                 / \
                6   9
            
Деревья бывают разных типов, но наиболее распространены двоичные деревья поиска. 
У них есть следующие особенности:
● У каждого узла не больше двух дочерних.
● Если новое значение меньше, оно становится левым дочерним либо дочерним левого дочернего.
● Если значение больше, оно становится правым дочерним или дочерним правого дочернего.

Как применяют двоичные деревья:
● Для быстрого поиска данных.
● Для хранения данных в отсортированном виде с возможностью быстро их добавлять и удалять.

Основные операции:

* Append() - Вставка заданного значения
* Delete() - Удаление узла с нужны значением
* Find() - Поиск по дереву 
"""


class Node:
    """Узел дерева"""

    def __init__(self, data: Number = None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return repr(f"<Node data={self.data}>")

    @property
    def has_left_branch(self):
        return self.left is not None

    @property
    def has_right_branch(self):
        return self.right is not None

    @property
    def has_children(self):
        return bool(self.left) and bool(self.right)


class Tools:

    def find(
            self,
            node: Node,
            parent: Node | None,
            value: Number,
    ) -> tuple[Node | None, Node | None, bool]:
        """Поиск 'лево-корень-право'"""
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.has_left_branch:
                return self.find(node.left, node, value)

        if value > node.data:
            if node.has_right_branch:
                return self.find(node.right, node, value)

        return node, parent, False

    @staticmethod
    def del_leaf(node: Node, parent: Node):
        """Удаление 'листка' дерева"""
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    @staticmethod
    def del_one_child(node: Node, parent: Node):
        """Удаление узла с одной дочерней ветвью"""
        match node:
            case parent.left:
                if not node.has_left_branch:
                    parent.left = node.right
                elif not node.has_right_branch:
                    parent.left = node.left

            case parent.right:
                if not node.has_left_branch:
                    parent.right = node.right
                elif not node.has_right_branch:
                    parent.right = node.left

    def find_min(self, node: Node, parent: Node):
        """Поиск минимума"""
        if node.has_left_branch:
            return self.find_min(node.left, node)
        return node, parent

    def find_max(self, node: Node, parent: Node):
        """Поиск максимума"""
        if node.has_right_branch:
            return self.find_max(node.right, node)
        return node, parent


class Tree:
    """Бинарное дерево"""

    def __init__(self):
        self.tools = Tools()
        self.root: Node | None = None

    def append(self, obj: Node) -> Node:
        """Вставка данных"""
        if self.root is None:
            self.root = obj
            return obj

        node, parent, found = self.tools.find(self.root, None, obj.data)

        if not found and node:
            if obj.data < node.data:
                node.left = obj
            else:
                node.right = obj

        return obj

    def delete(self, key: Number):
        """Удаление узла"""
        node, parent, found = self.tools.find(self.root, None, key)

        if not found:
            return

        if not node.has_left_branch and not node.has_right_branch:
            self.tools.del_leaf(node, parent)

        if not node.has_left_branch or not node.has_right_branch:
            self.tools.del_one_child(node, parent)

        else:
            right_node, right_parent = self.tools.find_min(node.right, node)
            node.data = right_node.data
            self.tools.del_one_child(right_node, right_parent)

    def find(self, key: Number) -> Node | None:
        """Поиск узла со значением key"""
        node, _, found = self.tools.find(self.root, None, key)
        if found:
            return node
        return None

    def show(self, node: Node):
        """Вывод дерева"""
        if node is None:
            return

        self.show(node.left)
        print(node.data)
        self.show(node.right)

    @staticmethod
    def print(node: Node):
        """Вывод в ширину"""
        if node is None:
            return

        layer = [node, ]
        while layer:
            children = []
            for item in layer:
                print(item.data, end='\t')

                if item.has_left_branch:
                    children.append(item.left)
                if item.has_right_branch:
                    children.append(item.right)
            print()
            layer = children


if __name__ == "__main__":
    values = [20, 5, 24, 2, 16, 11, 18]
    tree = Tree()

    for x in values:
        tree.append(Node(x))

    # tree.show(tree.root)
    tree.delete(5)
    tree.print(tree.root.left)
    print(tree.find(11))
