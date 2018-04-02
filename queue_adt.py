class ArrayQueue():

    def __init__(self, capacity):

        self._capacity = capacity
        self._front = 0
        self._size = 0
        self._data = self._capacity*[None]

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def get_capacity(self):

        return self._capacity

    def front(self):

        return self._data[self._front]

    def dequeue(self):

        if 0 < self._size < self._capacity//4:

            self.resize(self._capacity//2)

        if self._size == 0:

            raise IndexError("Queue is currently empty")
        else:
            ans = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1)%self._capacity
            self._size -= 1
            return ans

    def enqueue(self, element):
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        self._data[(self._front + self._size) % self._capacity] = element
        self._size += 1

    def resize(self, cap):

        old_data = self._data
        self._data = cap*[None]
        walk = self._front
        for k in range(self._size):
            self._data[k] = old_data[walk]
            walk = (walk + 1)%self._capacity
        self._capacity = cap
        self._front = 0

    def __str__(self):

        ans = ""
        walk = self._front
        for k in range(self._size):

            ans = ans + str(self._data[walk]) + ", "
            walk = (walk +1)%self._capacity
        return ans

if __name__ == "__main__":

    queue = ArrayQueue(10)

    for k in range(6):
        queue.enqueue(k)

    print(queue)

    for k in range(3):

        queue.dequeue()

    print(queue)

    for k in range(20):

        queue.enqueue(k)
        print(queue)
        print(queue.get_capacity())

    for k in range(20):

        queue.dequeue()
        print(queue)
        print(queue.get_capacity())






