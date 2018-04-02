class CircularQ:

    class _Node:

        __slots__ = "_element","_next"

        def __init__(self, element, link):

            self._element = element
            self._next = link

    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):

        if self.is_empty():
            raise IndexError("Queue is currently empty")
        else:
            return self._tail._next._element

    def enqueue(self, element):

        new = self._Node(element,None)
        if self._size == 0:
            new._next = new
            self._tail = new
        else:
            new._next = self._tail._next
            self._tail._next = new
            self._tail = new
        self._size += 1

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Queue is currently Empty")
        else:
            ans = self._tail._next
            if self._size == 1:
                self._tail = None
                self._size -=1
                return ans
            else:
                self._tail._next = ans._next
                self._size -= 1
                return ans

    def rotate(self):

        if not(self.is_empty()):
            self._tail = self._tail._next

    def __str__(self):

        ans =""
        curr = self._tail
        for i in range(self._size):
            ans = ans + str(curr._element) + " -- "
            curr = curr._next
        return ans

if __name__ == "__main__":

    c_queue = CircularQ()

    for i in range(20):
        c_queue.enqueue(i)

    for i in range(len(c_queue)):
        print(c_queue)
        c_queue.rotate()





