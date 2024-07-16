class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[self._parent(index)][0] < self.heap[index][0]:
            self.heap[self._parent(index)], self.heap[index] = self.heap[index], self.heap[self._parent(index)]
            index = self._parent(index)

    def _heapify_down(self, index):
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left

        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)

    def insert(self, key, value):
        self.heap.append((key, value))
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
        else:
            self.heap.pop()
        return root

    def heapify(self, array):
        self.heap = array
        for i in range(len(array) // 2, -1, -1):
            self._heapify_down(i)

    def remove_max(self):
        return self.extract_max()
