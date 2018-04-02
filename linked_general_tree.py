import trees_abstract_base_class

class LinkedGeneralTree(trees_abstract_base_class.Tree):

    class _Node:

        __slots__ = "_element","_children","_parent"

        def __init__(self,element,parent):

            self._element = element
            self._parent = parent
            self._children = []

    class Position:

        def __init__(self, container, node):

            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return (type(self) == type(other)) and (self._node == other._node)

    def _validate(self,p):

        if not(isinstance(p,self.Position)):
            raise ValueError("Object not of type Position")
        if p._container != self:
            raise ValueError("This position does not belong to this tree")
        if p._node._parent == p._node:
            raise ValueError("This position is no longer valid")
        return p._node

    def _make_position(self,node):

        if node is not None:
            return self.Position(self,node)
        else:
            return None

    def __init__(self):

        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self,p):

        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self,p):

        node = self._validate(p)
        return len(node._children)

    def children(self,p):

        node = self._validate(p)
        for k in node._children:
            yield self._make_position(k)

    def is_root(self,p):
        return self._validate(p) != self._root

    def add_root(self,element):

        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(element,None)
        self._size += 1
        return self._make_position(self._root)

    def add_child(self,p,element):

        node = self._validate(p)
        node._children.append(self._Node(element,node))
        self._size += 1
        return self._make_position(node._children[-1])

    def replace(self,p,element):

        node = self._validate(p)
        node._element = element
        return self._make_position(node)

    def delete(self,p):

        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError("Cannot delete node with more than one child")
        if node == self._root:
            if len(node._children) == 0:
                self._root = None
                self._size -= 1
                node._parent = node
            else:
                self._root = node._children[0]
                self._size -= 1
                node._parent = node
        else:
            parent = node._parent
            if len(node._children) == 0:
                child = None
            else:
                child = node._children[0]

            index = parent._children.index(node)
            if child is not None:
                parent._children[index] = child
            else:
                del parent._children[index]
            self._size -= 1
            node._parent = node

if __name__ == "__main__":

    g_tree = LinkedGeneralTree()




