# Класс СНМ с эвристиками ранга и сжатия путей
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
