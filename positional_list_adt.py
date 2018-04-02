import doubly_linked_list_adt

class PositionalList(doubly_linked_list_adt._DoublyLinkedListBase):

    class _Position:

        def __init__(self, container, node):

            self._container = container
            self._node = node

        def element(self):

            return self._node._element

        def __eq__(self, other):

            return type(self) == type(other) and self._node == other._node

        def __ne__(self, other):

            return not (self == other)

    def _validate(self, p):

        if not isinstance(p,self._Position):
            raise TypeError("Object is not of type Position")
        else:
            if p._container is not self:
                raise ValueError("This position does not belong to this container")
            else:
                if p._node._next == None:
                    raise ValueError("p is no longer a valid position")
        return p._node

    def make_position(self, node):

        if node == self._header or node == self._trailer:
            return None
        else:
            return self._Position(self,node)

    def first(self):

        return self.make_position(self._header._next)

    def last(self):

        return self.make_position(self._trailer._prev)

    def before(self,p):

        node = self._validate(p)
        return self.make_position(node._prev)

    def after(self,p):

        node = self._validate(p)
        return self.make_position(node._next)

    def __iter__(self):

        cursor = self.first()
        while cursor != None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_node(self, element, pred, succ):

        node = super().insert_node(element, pred, succ)
        return self.make_position(node)

    def add_first(self, element):

        return self.insert_node(element,self._header,self._header._next)

    def add_last(self, element):

        return self.insert_node(element, self._trailer._prev, self._trailer)

    def add_before(self, element, p):

        node = self._validate(p)
        return self.insert_node(element,node._prev,node)

    def add_after(self, element, p):

        node = self._validate(p)
        return self.insert_node(element,node,node._next)

    def delete(self,p):

        node = self._validate(p)
        self.delete_node(node)

    def replace(self,p,element):

        node = self._validate(p)
        old_val = node._element
        node._element = element
        return old_val


def positional_sort(p):

    if len(p) > 1:

        marker = p.first()
        while marker != p.last():
            pivot = p.after(marker)
            value = pivot.element()
            if value >= marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != p.first() and p.before(walk).element() > value:
                    walk = p.before(walk)
                p.delete(pivot)
                p.add_before(value,walk)

    return p


if __name__ == "__main__":

    p = PositionalList()

    for i in range(20):
        p.add_last(i)
        print(p)

    print(positional_sort(p))





