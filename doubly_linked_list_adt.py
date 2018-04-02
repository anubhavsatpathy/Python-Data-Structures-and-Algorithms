class _DoublyLinkedListBase:

    class _Node:

        __slots__ = "_element","_prev","_next"

        def __init__(self, element, pred, succ):

            self._element = element
            self._prev = pred
            self._next = succ

    def __init__(self):

        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_node(self, element, pred, succ):

        node = self._Node(element, pred, succ)
        pred._next = node
        succ._prev = node
        self._size += 1
        return node

    def delete_node(self, node):

        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None
        return element

    def __str__(self):

        ans ="HEADER --"
        walk = self._header
        while walk._next !=self._trailer:
            ans = ans + str(walk._next._element)+ " -- "
            walk = walk._next
        return ans + "TRAILER"


class LinkedDQ(_DoublyLinkedListBase):

    def first(self):

        if self.is_empty():
            raise IndexError("DQ currently empty")
        else:
            return self._header._next._element

    def last(self):

        if self.is_empty():
            raise IndexError("DQ currently empty")
        else:
            return self._trailer._prev._element

    def enqueue(self, element, pos = "FIRST"):

        if pos == "FIRST":
            self.insert_node(element,self._header,self._header._next)
        else:
            if pos == "LAST":
                self.insert_node(element, self._trailer._prev, self._trailer)
            else:
                raise ValueError("Invalid Positional Argument - allowed values - FIRST and LAST")

    def dequeue(self, pos = "FIRST"):

        if self.is_empty():
            raise IndexError("Q is currently empty")
        if pos == "FIRST":
            return self.delete_node(self._header._next)
        else:
            if pos == "LAST":
                return self.delete_node(self._trailer._prev)
            else:
                raise ValueError("Invalid Positional Argument - allowed values - FIRST and LAST")



if __name__ == "__main__":

    ldq = LinkedDQ()

    for i in range(10):
        ldq.enqueue(i)
        print(ldq)

    for i in range(len(ldq)):
        ldq.enqueue(i*100,pos="LAST")
        print(ldq)

    for i in range(len(ldq)//2):
        ldq.dequeue()
        print(ldq)

    for i in range(len(ldq)):
        ldq.dequeue(pos="LAST")
        print(ldq)



