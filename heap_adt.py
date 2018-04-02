class MinHeap:

    def __init__(self):

        self._data = []

    def _parent(self,j):

        return (j-1)//2

    def _left(self,j):

        return 2*j +1

    def _right(self,j):

        return 2*j + 2

    def __len__(self):

        return len(self._data)

    def _has_left(self,j):

        return (2*j + 1) < len(self)

    def _has_right(self,j):

        return (2*j + 2) < len(self)