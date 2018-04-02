class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        """
        Constructor for the adapter class to implement a stack using a python list
        """
        self._stack = []

    def __len__(self):

        return len(self._stack)

    def top(self):

        if self.is_empty():
            raise Empty("Stack is empty")

        return self._stack[-1]

    def push(self, element):

        self._stack.append(element)

    def is_empty(self):

        return len(self._stack) == 0

    def pop(self):

        if self.is_empty():
            raise Empty("Stack is currently empty")
        else:
            return self._stack.pop()

    def __str__(self):

        return str(self._stack)


if __name__ == "__main__":

    ex_stack =ArrayStack()

    print("Default stack length : {}".format(len(ex_stack)))
    b = ex_stack.top()


