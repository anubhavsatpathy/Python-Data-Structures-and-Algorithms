class LinkedQ:

    class _Node:

        __slots__ = "_element","_next"

        def __init__(self, element, link):

            self._element = element
            self._next = link


    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):

        return self._size

    def enqueue(self, element):

        if self._size == 0:

            self._head = self._tail = self._Node(element,None)
            self._size += 1

        else:

            self._tail._next = self._Node(element,None)
            self._tail = self._tail._next
            self._size += 1

    def dequeue(self):

        if self._size == 0:

            raise IndexError("Queue is currentlu empty")
        else:

            ans = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self._size == 0:

                self._tail = None
            return ans

    def first(self):

        if self._size == 0:
            raise IndexError("Queue is currently empty")
        else:
            return self._head._element

    def __str__(self):

        if self._size == 0:
            return "Empty Queue"
        else:
            ans = "HEAD -- "
            walk = self._head
            while walk != None:

                ans = ans + str(walk._element) + " -- "
                walk = walk._next

            ans = ans + "TAIL -- "

            return ans

if __name__ == "__main__":

    l_queue = LinkedQ()

    for i in range(20):
        l_queue.enqueue(i)
        print(l_queue)

    for i in range(20):
        l_queue.dequeue()
        print(l_queue)