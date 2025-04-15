class UnionFind:
    def __init__(self, x: int):
        self.parent = [i for i in range(x)]
        self.size = [1] * x
        self.num_components = x


    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        # path compression makes this an inverse Ackermann function
            

    def isSameComponent(self, x : int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        root_of_x = self.find(x)
        root_of_y = self.find(y)
        if root_of_x != root_of_y:
            if self.size[root_of_x] < self.size[root_of_y]:
                self.parent[root_of_x] = self.parent[root_of_y]
                self.size[root_of_y] += self.size[root_of_x]
            else:
                self.parent[root_of_y] = self.parent[root_of_x]
                self.size[root_of_x] += self.size[root_of_y]
            self.num_components -= 1
            return True
        return False


    def getNumComponents(self) -> int:
        return self.num_components    



'''
Time: O(a(n)) != O(1)
! very slow growing so it executes like an constant time operation
find() -> O(n) recursiverly n + n
isSameComponent() -> o(n) calls find()
union() -> O(n) calls find
getNumComponents -> O(1)


space:
class itself is O(n)
all functions are O(1) union no new memory allocated during runtime
'''