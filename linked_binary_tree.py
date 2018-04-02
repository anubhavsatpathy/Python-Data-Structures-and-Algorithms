import binary_trees_abstract_base_class
import linked_queue_adt

class LinkedBinaryTree(binary_trees_abstract_base_class.BinaryTree):

    class _Node:

        __slots__ = "_element","_parent","_left","_right"

        def __init__(self, element, parent, left, right):

            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:

        def __init__(self, container, node):

            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            return (type(other) is type(self)) and (self._node is other._node)

        def __ne__(self, other):

            return not(self == other)

    def _validate(self,p):

        if not isinstance(p, self.Position):
            raise ValueError("Not of type Position")
        if p._container != self:
            raise ValueError("Position does not belong to this tree")
        if p._node._parent == p._node:
            raise ValueError("This position is no longer valid")
        return p._node

    def _make_position(self, node):

        if node is not None:
            return self.Position(self,node)
        else:
            return None

    def __init__(self, traverse_method = "inorder"):

        self._root = None
        self._size = 0
        self._traverse = traverse_method

    def set_traversal(self,t):
        self._traverse = t

    def __len__(self):

        return self._size

    def root(self):

        return self._make_position(self._root)

    def parent(self,p):

        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self,p):

        node = self._validate(p)
        return self._make_position(node._left)

    def right(self,p):

        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self,p):

        if (self.left(p) is not None) and (self.right(p) is not None):
            return 2
        if ((self.right(p) is None) and (self.left(p) is not None)) or ((self.right(p) is not None) and (self.left(p) is None)):
            return 1
        if (self.right(p) is None) and (self.left(p) is None):
            return 0

    def add_root(self, element):

        if self.root() is not None:
            raise ValueError("Root Already Exists")
        else:
            self._root =self._Node(element,None,None,None)
            self._size += 1
            return self._make_position(self._root)

    def add_left(self,pos,elemet):

        node = self._validate(pos)
        if node._left is not None:
            raise ValueError("Left Node already exists")
        else:
            node._left = self._Node(elemet,node,None,None)
            self._size += 1
            return self._make_position(node._left)

    def add_right(self, pos, element):

        node = self._validate(pos)
        if node._right is not None:
            raise ValueError("Right node already exists")
        else:
            node._right = self._Node(element,node,None,None)
            self._size += 1
            return self._make_position(node._right)

    def replace(self, pos, element):

        node = self._validate(pos)
        node._element = element
        return self._make_position(node)

    def delete(self,pos):

        node = self._validate(pos)
        if self.num_children(pos) == 2:
            raise ValueError("Position has two children")
        child = None
        if node._left is None:
            child = node._right
        else:
            child = node._left
        if node == self._root:
            self._root = child
            self._size -= 1
            if child is not None:
                child._parent = None
            node._parent = node
            return node._element
        else:
            parent = node._parent
            if parent._left == node:
                parent._left = child
            else:
                parent._right = child
            if child is not None:
                child._parent = parent
            self._size -= 1
            node._parent = node
            return node._element

    def attach(self,pos,t1,t2):

        if not(self.is_leaf(pos)):
            raise ValueError("Position must be a leaf")
        if not(type(self) == type(t1) == type(t2)):
            raise ValueError("T1 or T2 are not LinkedBinaryTrees")
        node = self._validate(pos)
        if not(t1.is_empty()):
            t1._root._parent = node
            node._left = t1._root
            self._size += len(t1)
            t2._root = None
            t1._size = 0
        if not(t2.is_empty()):
            t2._root._parent = node
            node._right = t2._root
            self._size += len(t2)
            t2._root = None
            t2._size = 0

    def __iter__(self):

        for p in self.positions():
            yield p.element()

    def positions(self, flag = "inorder"):
        if flag == "preorder" and (not self.is_empty()):
            for p in self.preorder(self.root()):
                yield p
        if flag == "postorder" and (not self.is_empty()):
            for p in self.postorder(self.root()):
                yield p
        if flag == "breadthfirst" and (not self.is_empty()):
            for p in self.breadth_first():
                yield p
        if flag == "inorder" and (not self.is_empty()):
            for p in self.inorder(self.root()):
                yield p

    def preorder(self, pos):
        yield pos
        for c in self.children(pos):
            for other in self.preorder(c):
                yield other

    def postorder(self, pos):
        for c in self.children(pos):
            for other in self.postorder(c):
                yield other
        yield pos

    def breadth_first(self):
        if not self.is_empty():
            queue = linked_queue_adt.LinkedQ()
            queue.enqueue(self.root())
            while len(queue) != 0:
                p = queue.dequeue()
                yield p
                for c in self.children(p):
                    queue.enqueue(c)

    def inorder(self, pos):
        if self.left(pos) is not None:
            for c in self.inorder(self.left(pos)):
                yield c
        yield pos
        if self.right(pos) is not None:
            for c in self.inorder(self.right(pos)):
                yield c




if __name__ == "__main__":

    b_tree = LinkedBinaryTree()
    p = b_tree.add_root(1)
    l = b_tree.add_left(p,2)
    r = b_tree.add_right(p,3)
    ll= b_tree.add_left(l,4)
    lr = b_tree.add_right(l,5)

    for i in b_tree:
        print(i)
    print("_____________________________")
    for i in b_tree.postorder(b_tree.root()):
        print(i)







