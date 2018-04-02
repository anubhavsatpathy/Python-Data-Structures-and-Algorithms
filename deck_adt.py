class Deck():

    def __init__(self, capacity):

        self._data = capacity*[None]
        self._capacity =capacity
        self._front = 0
        self._size = 0

    def __len__(self):

        return self._size

    def is_empty(self):

        return self._size == 0

    def resize(self, cap):

        old_data = self._data
        self._data = cap * [None]
        walk = self._front

        for k in range(self._size):

            self._data[k] = old_data[walk]
            walk = (walk + 1)%self._capacity

        self._front = 0
        self._capacity = cap

    def add_first(self, element):

        if self._size == self._capacity:

            self.resize(self._capacity*2)

        self._front = (self._front - 1)%self._capacity
        self._data[self._front] = element
        self._size += 1

    def add_last(self, element):

        if self._size == self._capacity:

            self.resize(self._capacity * 2)

        self._data[(self._front + self._size)%self._capacity] = element
        self._size += 1

    def del_first(self):

        if 0 < self._size < (self._capacity//4):

            self.resize(self._capacity//2)

        if self._size == 0:

            raise IndexError("Deck is currently empty")

        else:

            ans = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front+ 1)%self._capacity
            self._size -= 1
            return ans

    def del_last(self):

        if 0 < self._size < (self._capacity // 4):
            self.resize(self._capacity // 2)

        if self._size == 0:
            raise IndexError("Deck is currently empty")

        else:

            ans = self._data[(self._front + self._size - 1)%self._capacity]
            self._data[(self._front + self._size - 1) % self._capacity] = None
            self._size -=1
            return ans

    def __str__(self):

        ans = ""

        walk = self._front

        for k in range(self._size):

            ans = ans + str(self._data[walk]) + ", "
            walk = (walk+1)%self._capacity

        return ans


if __name__ == "__main__":

    deck = Deck(10)

    for i in range(20):

        deck.add_first(i)
        print(deck)

    for i in range(len(deck)):
        deck.del_last()
        print(deck)



