class UnionFind:
    def __init__(self):
        self._id = []
        self._rank = []

    def make_set(self, x):
        self._id.append(x)
        self._rank.append(0)

    def __str__(self):
        ret = " ".join(list(map(str, self._id))) + "\n" + " ".join(list(map(str, self._rank)))
        return ret

    def root(self, x):
        if x == self._id[x]:
            return x
        self._id[x] = self.root(self._id[x])
        return self._id[x]

    def union_set(self, x, y):
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:
            return
        if self._rank[x_root] < self._rank[y_root]:
            self._id[x_root] = y_root
        else:
            self._id[y_root] = x_root
            if self._rank[x_root] == self._rank[y_root]:
                self._rank[x_root] += 1

    def connected(self, x, y):
        return self.root(x) == self.root(y)


def Kruskal_MST(N, edges):
    """
    >>> Kruskal_MST(7, [(0, 3, 1), (4, 5, 2), (3, 2, 2), (0, 1, 5), (3, 1, 6), (0, 4, 8), (2, 6, 9), (1, 2, 10), (5, 3, 12), (3, 6, 15)])
    (0, 1) (0, 3) (0, 4) (2, 6) (3, 2) (4, 5) 1
    """
    ostov = UnionFind()
    for i in range(N):
        ostov.make_set(i)

    ostov_to_print = [[] for _ in range(N)]
    # сортируем список ребер
    edges.sort(key=lambda edge: edge[2])  # по весу

    for edge in edges:
        if not ostov.connected(edge[0], edge[1]):
            ostov.union_set(edge[0], edge[1])
            ostov_to_print[edge[0]].append(edge[1])
    return print_spanning_tree(ostov_to_print)


def print_spanning_tree(A):
    res = []
    for u, nei in enumerate(A):
        for v in nei:
            res.append((u, v))
    res.sort(key=lambda edge: (edge[0], edge[1]))
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

