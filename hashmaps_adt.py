import random

class MapBase:

    class _Item:

        __slots__ = "_key","_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):

            return self._key == other._key

        def __ne__(self, other):

            return not(self == other)

        def __lt__(self, other):

            return self._key < other._key

class UnsortedMap(MapBase):

    def __init__(self):

        self._table = []

    def __len__(self):

        return len(self._table)

    def __getitem__(self, k):

        if len(self) == 0:
            raise KeyError("Invalid Key")
        else:
            for item in self._table:
                if item._key == k:
                    return item._value

    def __setitem__(self, key, value):

        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key,value))

    def __delitem__(self, key):

        if len(self) == 0:
            raise KeyError("Invalid Key")
        else:
            for item in self._table:
                if key== item._key:
                    self._table.pop(item)
            return KeyError("Invalid Key")

    def __iter__(self):

        for item in self._table:
            yield item._key

class HashMap(MapBase):

    def __init__(self, cap, prime):

        self._table = cap*[None]
        self._prime = prime
        self._scale = 1 + random.randrange(prime - 1)
        self._shift = random.randrange(prime)
        self._n = 0

    def _hashfunc(self,key):

        return [(hash(key)*self._scale)+self._shift]%self._prime%len(self._table)

    def __len__(self):

        return self._n

    def __iter__(self):

        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

    def items(self):

        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield (key,bucket[key])


    def __getitem__(self, key):

        j = self._hashfunc(key)
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("No Such Key Exists")
        else:
            return bucket[key]

    def __setitem__(self, key, value):

        j = self._hashfunc(key)
        bucket = self._table[j]
        if bucket is None:
            bucket = UnsortedMap()
        old_size = len(bucket)
        bucket[key] = value
        if len(bucket)>old_size:
            self._n += 1
        if self._n > len(self._table)//2:
            self.resize(2*len(self._table) - 1)


    def resize(self,new_size):

        old = list(self.items())
        self._table = new_size*[None]
        self._n = 0
        for (k,v) in old:
            self[k] = v





