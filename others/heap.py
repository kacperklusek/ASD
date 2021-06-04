
class MaxHeap:
    def __init__(self, h):
        self.maxsize = 100
        self.heap = h + [0 for _ in range(self.maxsize - len(h))]
        self.maximum = self.heap[0]
        self.size = len(h)

    def __str__(self):
        print(self.heap)
        i = 0
        h = self.heap
        for idx in range(self.size):
            print(h[idx])
            if idx == 2**i:
                print()
                i += 1

    def parent(self, idx):
        return self.heap[(idx-1)//2]

    def right_child(self, idx):
        return self.heap[2 * idx + 1]

    def left_child(self, idx):
        return self.heap[2 * idx + 2]

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def get_val(self, idx):
        return self.heap[idx]

    def insert(self, val):
        idx = self.size + 1
        self.heap[idx] = val
        while self.parent(idx) < self.heap[idx]:
            self.swap(self.parent(idx), self.heap[idx])

    def heapify(self, idx):
        heap = self.heap
        while (2*idx + 1 < self.size and self.left_child(idx) > heap[idx]) or \
                (2*idx + 2 < self.size and self.right_child(idx) > heap[idx]):
            if self.left_child(idx) >= self.right_child(idx):
                self.swap(idx, 2*idx + 1)
                idx = 2 * idx + 1
            else:
                self.swap(idx, 2*idx + 2)
                idx = 2 * idx + 2

    def buildheap(self):
        n = self.size
        for i in range((n-1)//2, -1, -1):
            self.heapify(i)

heap = MaxHeap([1,2,7,12,10,17])
heap.buildheap()
print(heap)

