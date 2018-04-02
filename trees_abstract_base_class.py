class Tree:

    class Position:

        def element(self):
            raise NotImplementedError("Method not Implemented")
        def __eq__(self, other):
            raise NotImplementedError("Method not implemented")
        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError("Method not Implemented")
    def parent(self,p):
        raise NotImplementedError("Method not Implemented")
    def num_children(self,p):
        raise NotImplementedError("Method not Implemented")
    def children(self,p):
        raise NotImplementedError("Method not Implemented")
    def __len__(self):
        raise NotImplementedError("Method not Implemented")
    def is_root(self,p):
        return p == self.root()
    def is_empty(self):
        return len(self) == 0
    def is_leaf(self,p):
        return self.num_children(p) == 0
    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    def height(self,p = None):
        if p == None:
            p = self.root()
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(k) for k in self.children(p))



