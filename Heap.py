class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, p):
        if p == 0:
            return 0
        return (p - 1) // 2

    def sift_up(self, p):
        heap = self.heap
        if heap[p] == heap[0]:
            return
        while heap[self.parent(p)] > heap[p]:
            if p == 0:
                return
            heap[p], heap[self.parent(p)] = heap[self.parent(p)], heap[p]
            p = self.parent(p)

    def left_son(self, p):
        return 2 * p + 1

    def right_son(self, p):
        return 2 * p + 2

    def min_son(self, p):
        heap = self.heap
        if self.left_son(p) >= len(heap) - 1:
            return -1
        if self.right_son(p) < len(heap):
            if heap[self.left_son(p)] < heap[self.right_son(p)]:
                return self.left_son(p)
            else:
                return self.right_son(p)
        else:
            return self.left_son(p)

    def sift_down(self, p):
        heap = self.heap
        minCh = self.min_son(p)
        while minCh > 0 and heap[minCh] < heap[p]:
            heap[minCh], heap[p] = heap[p], heap[minCh]
            p = minCh
            minCh = self.min_son(p)

    def add(self, x):
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

    def min(self):
        return self.heap[0]

    def get_min(self):
        ret = self.heap[0]
        self.heap[-1], self.heap[0] = self.heap[0], self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 1:
            self.sift_down(0)
        return ret

    def __str__(self):
        return " ".join(list(map(str, self.heap)))
