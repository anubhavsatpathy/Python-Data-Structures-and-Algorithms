class LinkedStack:

    class Node:

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

    def push(self,element):

        self._head = self.Node(element,self._head)
        self._size += 1

    def pop(self):

        if self._size == None:

            raise ValueError("List is currently empty")

        else:

            ans = self._head._element
            self._head = self._head._next
            self._size -= 1
            return ans

    def top(self):

        return self._head._element



    def __str__(self):

        if self._size == None:

            return "Empty List"
        else:

            ans = ""
            walk = self._head
            while walk != None:

                ans = ans + str(walk._element) + ", "
                walk = walk._next
            return ans

if __name__ == "__main__":

    l_stack = LinkedStack()

    for i in range(20):
        l_stack.push(i)
        print(l_stack)

    for i in range(len(l_stack)):

        l_stack.pop()
        print(l_stack)





