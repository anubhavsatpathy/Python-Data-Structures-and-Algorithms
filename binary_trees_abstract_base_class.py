import trees_abstract_base_class

class BinaryTree(trees_abstract_base_class.Tree):

    def left(self,p):
        raise NotImplementedError("Method not Implemented")
    def right(self,p):
        raise NotImplementedError("Method not Implemented")
    def sibling(self,p):
        parent = self.parent(p)
        if parent == None:
            return None
        else:
            if p == self.right(parent):
                return self.left(parent)
            else:
                return self.right(parent)
    def children(self,p):
        if self.left(p) != None:
            yield self.left(p)
        if self.right(p) != None:
            yield self.right(p)


