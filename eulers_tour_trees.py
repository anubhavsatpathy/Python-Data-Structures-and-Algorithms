class EulersTour:

    def __init__(self, tree):
        self._tree = tree

    def pre_visit_action(self,pos, path, depth):
        pass

    def post_visit_action(self,pos,path,depth,results):
        pass

    def _tour(self, pos, path, depth):

        self.pre_visit_action(pos,path,depth)
        results = []
        path.append(0)
        for c in self._tree.children(pos):
            results.append(self._tour(c,path,depth+1))
            path[-1] += 1
        path.pop()
        answer = self.post_visit_action(pos,path,depth,results)
        return answer

    def excute(self):
        if len(self._tree) > 0:
            self._tour(self._tree.root(),[],0)



