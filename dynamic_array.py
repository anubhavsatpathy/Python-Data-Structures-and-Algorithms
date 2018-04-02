import ctypes
import sys

class D_Array:
    """
    A basic implementation of dynamic arrays that mimics the behavior of pythons built in list class
    """
    def __init__(self):
        """
        Constructor for the dynamic array object :
        1. Initialize object with capacity = 1
        2. Stores length = 0
        3. Creates a compact array using the c-types module
        """
        self._n = 0
        self._capacity = 1
        self._A = self.make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):

        if k > self._n:
            raise IndexError("Index out of range")
        else:
            return self._A[k]

    def append(self, obj):

        if self._n == self._capacity:
            self.resize()
        self._A[self._n] = obj
        self._n += 1

    def resize(self):

        B = self.make_array(self._capacity*2)
        for i in range(self._n):
            B[i] = self._A[i]

        self._A = B
        self._capacity = self._capacity * 2


    def make_array(self,c):
        return (c * ctypes.py_object)()

    def get_size(self):
        return sys.getsizeof(self._A)

a = D_Array()

#Find out how to convert python object to py_object references